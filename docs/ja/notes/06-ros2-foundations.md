# 6. ROS 2：分散ロボティクスソフトウェアと通信インターフェース

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](../../pt/notes/06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**このページの単位（例の前に説明）:** `m` — メートル; `s` — 秒. [単位一覧](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** 合成データを使ったソフトウェア学習専用です。実機のロボットや機械の操作に使わないでください。ROS の通信は運動学、リアルタイム制御、ハードウェア安全機能の代替ではありません。

ROS 2（Robot Operating System 2）は、ロボットを構成する分散ソフトウェアの通信基盤です。バックエンド開発者には、ノード（node）を論理的な計算コンポーネント、トピック（topic）を型付き非同期ストリーム、サービス（service）を RPC に近い仕組みとして考えると理解しやすくなります。ただし ROS 2 は中央ブローカーを前提にせず、一般に DDS による分散発見を使います。

![ROS 2 publisher and subscriber linked through a typed topic; a CLI process calls a service](../../../assets/figures/ros2-topic-service.svg)

![ROS 2 のソフトウェア層と独立したハードウェア安全境界](../../../assets/figures/ros2-software-layers.svg)

*通信基盤は低レベル制御や独立した安全機構を代替しません。*

## 学習の順序

1. [アーキテクチャ、middleware、ROS graph](#section-1)
2. [Nodes、topics、型付き messages](#section-2)
3. [Services、actions、parameters](#section-3)
4. [Packages、workspaces、colcon、ament](#section-4)
5. [ROS 2 CLI での検査](#section-5)
6. [Launch files](#section-6)
7. [tf2 と座標フレーム（coordinate frames）](#section-7)
8. [URDF と robot_state_publisher](#section-8)
9. [ros2_control とハードウェア境界](#section-9)
10. [QoS、DDS discovery、Docker](#section-10)
11. [実習：二つのノード、topic、service、launch](#section-11)
12. [用語と制限](#section-12)

<a id="section-1"></a>

## 1. アーキテクチャ、middleware、ROS graph

**課題：** カメラ、位置推定、計画などの独立したソフトウェアを連携させます。ROS 1 は名前の発見に中央 master を使いました。ROS 2 は RMW（ROS Middleware）を介して、通常は DDS/RTPS を使い、ROS 1 master なしで参加者を発見します。ROS graph は発見されたノード、トピック、サービス、アクションの集合です。ノードは論理単位で、複数ノードを一つのプロセスに置くことも、複数ホストへ分散させることもできます。発見は認証ではありません。

<a id="section-2"></a>

## 2. Nodes、topics、型付き messages

**課題：** 継続的な測定値を複数の利用者へ配信します。Publisher が topic へ型付きメッセージを送り、subscriber が非同期に受信します。std_msgs/msg/String のフィールドは string data で、Python と C++ の両方で共通のインターフェースです。/sample_source は /training/status へ sample N を送信し、/sample_monitor が受信数を数えます。depth 10 は永続ログではなく、新しい購読者は通常その後のメッセージを受け取ります。

**発見の流れの例：** `/sample_monitor` が発見される前に `/sample_source` が `sample 1` を送ったと仮定します。この実習の履歴ポリシーは `volatile` なので、過去のメッセージは自動再送されません。Publisher が動作を続けていても、Monitor は最初に `received 0 samples` と返すことがあります。互換性のある endpoints が発見されてから受信数が増えます。送信側の通し番号と受信側の件数は別の測定値であり、どちらもトランザクションの確認にはなりません。

**CLI が示す範囲：** `ros2 topic list -t` は発見された topic の名前と型を示しますが、**subscriber への配信成功を証明しません**。`ros2 topic info /training/status -v` は発見された endpoints と提供・要求 QoS を示します。Subscriber が 0 件でも、存在しない場合と discovery が未完了の場合があります。Endpoints は見えるのに受信できない場合、型と QoS の互換性、プロセスログ、`ROS_DOMAIN_ID` を確認します。これらは状態のスナップショットであり配信保証ではありません。実習コンテナ内で実行してください。

<a id="section-3"></a>

## 3. Services、actions、parameters

**課題：** データストリーム、短い問い合わせ、長時間処理を区別します。Service は request/response で、/training/count は std_srvs/srv/Trigger を使い success と message を返します。Action は goal、feedback、result、cancel を備え、移動目標などに適します。Parameter はノードが所有する設定値です。interval_s=1.0 はタイマー生成時に読み込まれ、その後値を変えてもタイマーは自動再構築されません。再試行時の安全な振る舞いはアプリ側で定義します。

応答の種類、処理時間、失敗時の扱いに合わせて通信方式を選びます。各方式は互換ではありません。

| 方式 | 流れ | 適した用途 | 同じものではない |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N subscribers | 継続的な状態・テレメトリ | 永続ログや確認済みトランザクション |
| Service | 要求 → 応答 | 短い問い合わせや範囲の限られた処理 | 完了保証付きコミットや長時間タスク |
| Action | 目標 → feedback/結果、任意の取消 | ナビゲーションや長い計算 | 周期的センサーストリーム |
| Parameter | ノードが所有する値 | `interval_s` などの設定 | 分散された単一のグローバル設定 DB |

この例では `/training/status` は topic、`/training/count` は service、`interval_s` はノードの parameter です。アプリケーションの action はありません。Service のタイムアウトはサーバーが処理しなかった証拠ではなく、再試行の安全性は処理の意味によって異なります。

<a id="section-4"></a>

## 4. Packages、workspaces、colcon、ament

**課題：** 依存関係を明示してビルドを再現します。package.xml はパッケージのメタデータ、ament_python/ament_cmake はビルド統合です。Workspace には通常 src、build、install、log があります。colcon はビルドを調整するツールで、通信ミドルウェアではありません。環境は ROS の underlay を source してから workspace の overlay を source します。telemetry_demo の setup.py は二つの実行エントリーと launch ファイルを登録します。

実際の `ros2/Dockerfile` では、**イメージのビルド**（`RUN`）と**コンテナ起動**（`CMD`）は別の段階です。ビルド時は ROS underlay を読み込み、その後 `colcon` でパッケージをビルドします。

**イメージビルド（`RUN`）：**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**コンテナ起動（`CMD`）：**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

起動時には新しいシェルで ROS underlay を**再び**読み込み、生成済みの workspace overlay を読み込んで launch ファイルを実行します。`package.xml` は依存関係を宣言し、`setup.py` は Python エントリーポイントと launch ファイルをインストールします。`build/` と `install/` は生成物なので、ソースコードを直接編集する場所ではありません。ビルド成功と実行準備完了は異なります。

<a id="section-5"></a>

## 5. ROS 2 CLI での検査

**課題：** 実際の ROS graph を観測します。ros2 node list/info でノード、topic list/info/echo でストリーム、interface show で型、service list/call・action list・param get で他の端点を確認します。/sample_source、/sample_monitor、/training/status、/training/count が見えるはずです。デモにはアプリケーションの action はありません。データが流れない場合は名前、型、QoS、ROS_DOMAIN_ID を調べます。

コンテナ内で ROS 環境を読み込んでから CLI を実行します：

```bash
ros2 node list
ros2 node info /sample_source
ros2 topic list -t
ros2 topic info /training/status -v
ros2 topic echo /training/status
ros2 interface show std_msgs/msg/String
ros2 service list -t
ros2 service call /training/count std_srvs/srv/Trigger "{}"
ros2 action list
ros2 param get /sample_source interval_s
```

<a id="section-6"></a>

## 6. Launch files

**課題：** 複数プロセスを同じ設定で起動します。demo.launch.py は二つの launch_ros.actions.Node を含む LaunchDescription を返し、interval_s=1.0 を指定します。Launch は引数、名前空間、remapping、他ファイルの取り込みを扱えます。起動完了と通信準備完了は別なので、discovery や再試行を考慮する必要があります。

**起動後の準備完了を観察する：** `launch_ros.actions.Node` は二つの**プロセス**を開始しますが、DDS の発見と最初の `/training/status` メッセージはその後に起こります。直ちに `/training/count` を呼ぶと `received 0 samples` という正常な応答になる場合があり、後で増加します。これはトランザクション喪失の証拠ではなく、service はモニターが受信した数だけを返します。`interval_s=1.0` はタイマー生成時に読み込まれ、動作中の周期を自動更新しません。

<a id="section-7"></a>

## 7. tf2 と座標フレーム（coordinate frames）

**課題：** camera_link の観測を base_link や map へ変換します。tf2 は回転と並進を含む時刻付きの変換を保存・検索します。固定取り付けには静的変換、動く関節には動的変換を使います。親子関係と時刻が一致していなければなりません。tf2 自体は順運動学・逆運動学や経路計画を解きません。数学は既存の座標系・Jacobian の章で扱います。

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**座標フレームの接続例（必須の構成ではありません）：** `map → odom → base_link → camera_link`。固定されたカメラと本体の間は `static` 変換ですが、移動する本体には `dynamic` 変換が必要です。時刻 *t* に `camera_link` で観測した点を `map` に変換するには、tf2 が**観測時刻の**変換チェーンを求める必要があります。フレームの欠落、木構造の切断、時刻に対応するデータ不足は lookup/extrapolation エラーになります。過去の観測に最新の変換を当てはめると誤った座標になり得ます。

**変換の向きと逆変換の例。** `base_link`（B）を親座標系、`tool`（T）を子座標系とします。相対回転がなく、親の X 正方向へ 0.1 m 並進している場合、**B で表した工具原点は基準原点より X 正側**にあります。逆に T で基準原点を表すと符号が逆になります。

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

この単純な符号反転が成立するのは**両座標系の向きが同じ場合だけ**です。一般には点座標の変換に回転と並進があり、逆変換では**両方**を戻す必要があります。正しい回転行列の逆行列は $R^T$ です。

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

別の姿勢として、共通 Z 軸の周りに T を +90° 回転し、B での並進 (0.1 m, 0 m) はそのままにします。この場合、T で表した B の原点は (0 m, +0.1 m) であり、**(−0.1 m, 0 m) ではありません**。T 内の点 (0 m, 0.05 m) も同じ行列で B に変換できます。

$$
R_{BT}=\begin{bmatrix}0 & -1\\1 & 0\end{bmatrix},\quad
\mathbf t_{BT}=\begin{bmatrix}0.1\\0\end{bmatrix}\ \mathrm{m},\quad
\mathbf t_{TB}=\begin{bmatrix}0\\0.1\end{bmatrix}\ \mathrm{m}.
$$

$$
\mathbf p_T=\begin{bmatrix}0\\0.05\end{bmatrix}\ \mathrm{m}
\Longrightarrow
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT}
=\begin{bmatrix}0.05\\0\end{bmatrix}\ \mathrm{m}.
$$

座標系と変換は**座標関係の記述**であって、装置を動かす指令ではありません。ROS 2 の並進は通常メートル単位を使いますが、[座標系の章](04-coordinate-frames.md#section-3)ではミリメートルを使うため、数値を混ぜる前に単位換算が必要です。静的変換は固定取付、動的変換は状態を更新するコンポーネントが配信します。過去の観測は観測時刻に対応する変換を使い、データ欠損も処理します。

<a id="section-8"></a>

## 8. URDF と robot_state_publisher

**課題：** 機構の共通モデルを定義します。URDF は link、joint、原点、軸、任意の visual/collision/inertial 情報を記述します。robot_state_publisher は URDF と関節位置（通常 /joint_states の sensor_msgs/msg/JointState）から変換を公開します。URDF だけではエンコーダ計測、シミュレーション、逆運動学の解は得られません。m、rad、座標軸と時刻を統一します。

**変換の入力：** URDF は `fixed` 関節と可動関節の構造を記述します。`robot_state_publisher` は固定関節の幾何から `static` 変換を発行し、可動関節については `/joint_states`（`sensor_msgs/msg/JointState`）にある角度・位置から `dynamic` 変換を発行します。URDF 自体は**関節位置を測定せず**、欠けた計測値も生成しません。長さはメートル、角度はラジアン、タイムスタンプは一貫させます。

<a id="section-9"></a>

## 9. ros2_control とハードウェア境界

**課題：** 制御アルゴリズムとドライバを分離します。ros2_control は controller manager、状態インターフェース（位置・速度）、指令インターフェース（位置・速度・effort）、ハードウェア抽象化を提供します。概念上は planner→controller→hardware interface→device で、状態がフィードバックされます。ROS メッセージは厳密なリアルタイム動作、電流制限、安全停止を保証しません。この学習例に実機はありません。

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**controller manager の役割：** `controller_manager` はコントローラのライフサイクルを管理し、リソースマネージャを介して状態インターフェース（state interfaces）と指令インターフェース（command interfaces）へのアクセスを調整します。コントローラは仮想例の `joint1/position` のような実測状態を読み、動作中のコントローラは互換性のある指令インターフェースを確保して目標値を書き込めます。実測値と目標値は同じではなく、使用中の指令インターフェースを複数のコントローラが自由に重複確保することもできません。これは topic の発見とは別の管理です。

**この実習の範囲：** `/training/status` と `/training/count` が示すのは topic と service であり、**`ros2_control` ではありません**。どちらの node もコントローラではなく、`controller_manager`、ハードウェアインターフェース、閉ループ制御は動作しません。smoke test が成功してもコントローラのライフサイクル、リアルタイム性、機器の安全性は検証されません。[ros2_control 公式ガイド](https://control.ros.org/jazzy/doc/getting_started/getting_started.html)を参照してください。

**次の実習：GUI なし ros2_control、TF2、仮想関節:** [次の実習：GUI なし ros2_control、TF2、仮想関節](07-ros2-control-lab.md). 新しい実習では URDF、GenericSystem、指令、状態、/joint_states、TF2、QoS、ARM64 ローダー診断を説明し、実機は制御しません。

**次の段階：ロボット全体構成。** [五段階の ROS 2 Mermaid 図](08-ros2-robot-architecture.md)は知覚、時刻指定 TF2、計画、動作制御、フィードバックをつなぎます。実機の流れは概念的です。

<a id="section-10"></a>

## 10. QoS、DDS discovery、Docker

**課題：** メッセージ欠落やノードが見つからない原因を分けます。QoS には reliable/best_effort、volatile/transient_local、history、depth があります。Subscriber が publisher より強い保証を要求すると、名前と型が一致しても通信できない場合があります。DDS は UDP multicast や動的ポートを使用することが多く、Docker Desktop、VPN、Firewall が discovery を妨げます。ROS_DOMAIN_ID を揃えます。デモは特権やホストポートを使わず一つのコンテナ内で完結します。

**QoS 不一致の例：** publisher が `best_effort` を提供し、subscriber が `reliable` を要求する場合、topic 名とメッセージ型が一致し、グラフに接続先が表示されても、要求が満たされず**メッセージが届かない**ことがあります。逆に、`best_effort` の subscriber は、他の QoS 条件も一致すれば `reliable` の publisher から受信できます。`volatile` は過去のメッセージを再生しません。`transient_local` は利用可能な対応 publisher が保持する有限の履歴を渡せますが、**永続的な分散ログではありません**。

**診断の順番：** 同じコンテナ内で `ROS_DOMAIN_ID=42` を確認し、`ros2 node list`、`ros2 topic info /training/status -v`（端点と QoS）、`docker compose logs demo`（プロセスログ）の順に調べます。グラフが空なら RMW/DDS、ネットワークインターフェース、ファイアウォールを確認します。TCP ポート公開だけでは DDS の問題全般は解決しません。この実習は複数ホスト間通信を検証していません。

[ROS 2 Jazzy の公式 QoS ドキュメント](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[別の手順：Compose や独自 Dockerfile を使わない公式 ROS イメージ](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. 実習：二つのノード、topic、service、launch

docker compose up --build -d を実行します。ログには発行・受信された sample と増加するカウンタが現れる想定です。Service の応答は success=True と received 12 samples などで、数値は実行時刻に依存します。[独立した GitHub Actions の Docker スモークテスト](../../../.github/workflows/ros2-live-smoke.yml) は**単一コンテナ内で実際にアプリケーションを起動**し、二つの ROS ノード、`/training/status` の型付きメッセージ受信、`/training/count` のサービス応答を確認しています。通常の静的 CI は ROS を実行しません。ただし、複数ホスト間の DDS、決定論的なリアルタイム性、実機や利用者の Docker 環境は未検証です。

[Source, expected results and troubleshooting](../../../ros2/README.md). From the repository root:

学習順序は、イメージにインストール済みの `demo_nodes_cpp` talker と `demo_nodes_py` listener、次にリポジトリでビルドする `telemetry_demo`、最後に `ros2_control` です。Dockerfile は標準デモを APT で導入し、`telemetry_demo` を `colcon` でビルドします。対話操作では**一つの Bash シェル**を開き、**新しいシェルごとに一回だけ**環境を読み込みます。独立した `docker compose exec` は `CMD` のシェル環境を引き継ぎません。

ホスト側でコンテナを起動し、対話シェルを開きます：

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

コンテナ内（ホストではない）で環境を一回読み込み、ROS グラフを調べます：

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

`exit` 後、ホストに戻って終了処理をします：

```bash
docker compose down
```

**CI の信頼境界：** 実際の ROS 2 Docker スモークテストは、関連する変更が `main` に取り込まれた後に自動実行するか、`main` 上の `workflow_dispatch` で手動実行します。`pull_request` の変更では実行しません。PR 側の Bash スクリプトや Dockerfile をホスト runner 上で直接実行する危険を避けるためです。マージ前の隔離された Python 検証は、ROS を実際に動かすテストの代わりにはなりません。変更をマージ前に独立してレビューし、マージ後に実際の結果を確認する必要があります。

<a id="section-12"></a>

## 12. 用語と制限

- **Node / process（ノード / プロセス）：** Node は名前のある ROS の論理コンポーネントで、一つの OS プロセスに複数の Node を配置できます。
- **ROS graph：** 現在発見できている通信エンドポイントの集合であり、永続的な中央レジストリや認可機構ではありません。
- **Topic（トピック）：** 複数の Publisher と Subscriber を持てる、名前付きの非同期データストリームです。
- **Message（メッセージ）：** ROS interface で定義される型付きデータで、任意の Python/C++ オブジェクトではありません。
- **Publisher / subscriber：** メッセージの送信側と受信側です。配信には発見と互換性のある QoS が必要です。
- **Service（サービス）：** 短い処理向けの型付き要求と応答です。タイムアウトだけではサーバが未実行とは判断できません。
- **Action（アクション）：** 目標、feedback、結果、キャンセル要求を扱います。要求したキャンセルは即時停止の保証ではありません。
- **Parameter（パラメータ）：** 個々の Node が所有する設定値で、変更しても既存タイマーの周期が自動的に変わるとは限りません。
- **RMW / DDS：** RMW はミドルウェアを抽象化し、DDS は一般的な発見・通信技術です。DDS 自体は認証を保証しません。
- **colcon / ament：** ワークスペースのビルド統括 / ROS パッケージのビルド統合であり、メッセージ転送ではありません。
- **Launch：** 起動するプロセスと構成の記述です。起動成功は通信準備完了を意味しません。
- **tf2：** 時刻付きの座標系変換の基盤であり、逆運動学ソルバーではありません。
- **URDF / robot_state_publisher：** ロボット構造モデル / モデルと現在の関節状態から変換を配信するコンポーネントです。
- **ros2_control：** コントローラのライフサイクルと管理された state/command インターフェースです。この topic/service 実習には含まれません。
- **QoS：** 要求と提供の配信・履歴ポリシーの互換性であり、永続イベントログや安全認証ではありません。

**バージョン情報（2026 年 11 月 13 日確認）：** ROS 2 Jazzy LTS のサポートは 2029 年 5 月まで、Lyrical LTS は 2031 年 5 月までです。Docker タグは不変のイメージ digest や apt パッケージのバージョンを固定しません。

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
