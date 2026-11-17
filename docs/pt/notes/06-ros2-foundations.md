# 6. ROS 2: software robótico distribuído e interfaces

**Languages:** [en](../../en/notes/06-ros2-foundations.md) · [fr](../../fr/notes/06-ros2-foundations.md) · [de](../../de/notes/06-ros2-foundations.md) · [it](../../it/notes/06-ros2-foundations.md) · [es](../../es/notes/06-ros2-foundations.md) · [pt](06-ros2-foundations.md) · [zh](../../zh/notes/06-ros2-foundations.md) · [ja](../../ja/notes/06-ros2-foundations.md) · [nb](../../nb/notes/06-ros2-foundations.md) · [ru](../../ru/notes/06-ros2-foundations.md) · [ko](../../ko/notes/06-ros2-foundations.md) · [fi](../../fi/notes/06-ros2-foundations.md) · [pl](../../pl/notes/06-ros2-foundations.md)

**Unidades aqui utilizadas (explicadas antes dos exemplos):** `m` — metro; `s` — segundo. [Glossário de unidades](../UNITS.md).

[Course index](../README.md) · [Coordinate frames](04-coordinate-frames.md) · [Jacobian](05-velocity-jacobian.md) · [Docker lab](../../../ros2/README.md)

> **Safety:** Exemplo de software sintético apenas. Não utilizar para comandar robôs ou máquinas reais: ROS não substitui cinemática, controlo em tempo real nem sistemas de segurança de hardware.

ROS 2 (Robot Operating System 2) liga componentes de software distribuídos de um robô. Para desenvolvedores backend, um node lembra um processo, um topic um fluxo tipado de eventos e um service uma RPC. A analogia é limitada: o ROS 2 normalmente usa DDS e descoberta distribuída, sem exigir um broker central.

![ROS 2 publisher and subscriber connected by a typed topic; a CLI client calls a service](../../../assets/figures/ros2-topic-service.svg)

![Camadas ROS 2 e separação da segurança e do hardware](../../../assets/figures/ros2-software-layers.svg)

*A comunicação não substitui o controlo de baixo nível e as proteções independentes.*

## Sequência de aprendizagem

1. [Arquitetura, middleware e grafo ROS](#section-1)
2. [Nodes, topics e mensagens tipadas](#section-2)
3. [Services, actions e parameters](#section-3)
4. [Packages, workspaces, colcon e ament](#section-4)
5. [Inspeção pela ROS 2 CLI](#section-5)
6. [Launch files](#section-6)
7. [tf2 e referenciais de coordenadas](#section-7)
8. [URDF e robot_state_publisher](#section-8)
9. [ros2_control e fronteira do hardware](#section-9)
10. [QoS, DDS discovery e Docker](#section-10)
11. [Prática: dois nodes, topic, service e launch](#section-11)
12. [Glossário e limites](#section-12)

<a id="section-1"></a>

## 1. Arquitetura, middleware e grafo ROS

**Problema:** sensores, localização e planeamento precisam de interfaces independentes. ROS 1 usava um master central para descobrir nomes; ROS 2 utiliza a abstração RMW e normalmente DDS/RTPS para descobrir participantes sem esse master. O grafo ROS inclui nodes, topics, services e actions descobertos. Vários nodes podem partilhar processo e processos podem correr em computadores distintos. Descoberta não é autenticação.

<a id="section-2"></a>

## 2. Nodes, topics e mensagens tipadas

**Problema:** transmitir medições contínuas para vários consumidores. Um publisher envia mensagens tipadas para um topic; subscribers recebem-nas assincronamente. std_msgs/msg/String define o campo string data, partilhado entre Python e C++. /sample_source publica em /training/status; /sample_monitor recebe e conta. Uma fila com depth 10 não guarda um histórico duradouro; um novo subscriber normalmente só vê futuras mensagens.

**Exemplo de discovery:** imaginemos que `/sample_source` publicou `sample 1` antes de `/sample_monitor` ser descoberto. Com a política de histórico `volatile` deste laboratório, a mensagem anterior não é reproduzida automaticamente. O monitor pode inicialmente responder `received 0 samples` apesar de o publisher continuar a publicar. A contagem pode aumentar após a descoberta de endpoints compatíveis. O número publicado e a contagem recebida medem coisas diferentes; nenhum é confirmação de transação.

**O que a CLI demonstra:** `ros2 topic list -t` mostra nomes e tipos dos topics descobertos, **não** prova entrega ao subscriber. `ros2 topic info /training/status -v` apresenta os endpoints descobertos e as QoS oferecidas/solicitadas. Zero subscribers pode significar que não estão presentes **ou** que discovery ainda decorre. Se os endpoints existem mas não chegam dados, verificar tipos, QoS, logs e `ROS_DOMAIN_ID`. São observações momentâneas, não garantias de entrega. Executar estes comandos dentro do contentor do laboratório.

<a id="section-3"></a>

## 3. Services, actions e parameters

**Problema:** distinguir stream, pedido curto e operação longa. Um service usa request/response: /training/count com std_srvs/srv/Trigger devolve success e message. Action gere goal, feedback, result e cancel, adequado à navegação. Um parâmetro pertence ao node: interval_s=1.0 configura o timer na criação. Alterá-lo depois não recria automaticamente o timer. Uma política de retry depende da idempotência da operação.

A escolha depende do tipo de resposta, duração e falhas possíveis. Estes mecanismos não são intercambiáveis:

| Mecanismo | Fluxo | Usar para | Não confundir com |
| --- | --- | --- | --- |
| Topic | Publisher → 0..N subscribers | Telemetria contínua | Registo persistente ou transação confirmada |
| Service | Pedido → resposta | Consulta rápida ou operação limitada | Commit garantido ou tarefa longa |
| Action | Objetivo → feedback/resultado, eventual cancelamento | Navegação ou cálculo prolongado | Fluxo periódico de sensor |
| Parameter | Valor de um node | Configuração como `interval_s` | Base de dados global distribuída |

Neste exemplo, `/training/status` é um topic, `/training/count` é um service e `interval_s` é um parâmetro do node; não há nenhuma action de aplicação. Um timeout não prova que o servidor deixou de executar o pedido: a repetição depende da semântica da operação.

<a id="section-4"></a>

## 4. Packages, workspaces, colcon e ament

**Problema:** compilar executáveis e dependências de forma reprodutível. package.xml declara um package; ament_python ou ament_cmake integra o build. Um workspace tem habitualmente src, build, install e log. colcon organiza a compilação, não comunica mensagens. Primeiro ativa-se o underlay ROS, depois o overlay do workspace. telemetry_demo define dois pontos de entrada em setup.py e instala o launch file.

No verdadeiro `ros2/Dockerfile`, a **construção da imagem** (`RUN`) e o **arranque do contentor** (`CMD`) são fases distintas. Na construção, apenas o underlay ROS é carregado antes de compilar com `colcon`:

**Construção da imagem (`RUN`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
colcon build --packages-select telemetry_demo
```

**Arranque do contentor (`CMD`):**

```bash
source /opt/ros/${ROS_DISTRO}/setup.bash
source /opt/training_ws/install/setup.bash
exec ros2 launch telemetry_demo demo.launch.py
```

No arranque, uma nova shell carrega **novamente** o underlay e depois o overlay do workspace, iniciando o ficheiro launch. `package.xml` declara dependências; `setup.py` instala os pontos de entrada Python e o ficheiro launch. `build/` e `install/` são produtos gerados, não locais para editar fontes. A compilação bem-sucedida não prova a disponibilidade da aplicação.

<a id="section-5"></a>

## 5. Inspeção pela ROS 2 CLI

**Problema:** observar o grafo realmente ativo. ros2 node list/info apresenta nodes; topic list/info/echo examina streams; interface show mostra tipos; service list/call, action list e param get verificam outros endpoints. O laboratório inclui /sample_source, /sample_monitor, /training/status e /training/count. Não há action próprio. Sem dados, verificar nomes, tipos, QoS e ROS_DOMAIN_ID.

The following commands run in a sourced ROS shell **inside the container**:

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

**Problema:** lançar vários processos de forma consistente. demo.launch.py devolve LaunchDescription com duas ações launch_ros.actions.Node e interval_s=1.0. Launch aceita argumentos, namespaces, remappings e ficheiros incluídos. Lançar processos não garante serviços prontos: readiness, erros e retries exigem lógica da aplicação.

**Observar a disponibilidade:** `launch_ros.actions.Node` inicia dois **processos**, mas a descoberta DDS e a primeira mensagem `/training/status` surgem depois. Uma chamada imediata a `/training/count` pode legitimamente devolver `received 0 samples`; o contador aumenta mais tarde. Não é prova de uma transação perdida: o service conta apenas as mensagens recebidas pelo monitor. `interval_s=1.0` é lido quando o temporizador é criado e não altera automaticamente o período em execução.

<a id="section-7"></a>

## 7. tf2 e referenciais de coordenadas

**Problema:** transformar leituras de camera_link para base_link ou map. tf2 guarda transforms com tempo, rotação e translação. Montagens fixas usam transforms estáticos; juntas móveis precisam de transforms dinâmicos. Relações pai-filho e timestamps devem ser consistentes. tf2 não calcula cinemática inversa/direta ou planeamento; as aulas de coordenadas e Jacobiano tratam da matemática.

[Coordinate frames](04-coordinate-frames.md) · [Velocity and Jacobian](05-velocity-jacobian.md)

**Exemplo de cadeia de referenciais (não obrigatória):** `map → odom → base_link → camera_link`. Uma câmara montada rigidamente tem uma transformação `static`; o movimento da base requer transformações `dynamic`. Para interpretar em `map` um ponto observado em `camera_link` no instante *t*, o tf2 precisa de encontrar a cadeia **no instante da medição**. Um referencial em falta, uma árvore desconexa ou um timestamp indisponível causa erro de lookup/extrapolation; utilizar a transformação mais recente para dados antigos pode gerar coordenadas erradas.

**Exemplo do sentido da transformação e da sua inversa.** `base_link` (B) é o referencial pai e `tool` (T) o filho. Sem rotação relativa, uma translação de 0.1 m ao longo do X positivo do pai coloca a origem da ferramenta **à frente da origem da base em B**. Ao descrever a base em T, o mesmo deslocamento tem sinal contrário:

$$
{}^{B}\mathbf p_{T}=(0.1, 0, 0)\ \mathrm{m},\qquad
{}^{T}\mathbf p_{B}=(-0.1, 0, 0)\ \mathrm{m}\quad (R=I).
$$

Esta simples inversão de sinal só funciona quando os eixos têm **a mesma orientação**. Em geral, a transformação aplica rotação e translação, e a inversa deve desfazer **ambas**; para uma matriz de rotação válida, $R^T$ é a inversa:

$$
\mathbf p_B=R_{BT}\mathbf p_T+\mathbf t_{BT},\qquad
\mathbf p_T=R_{BT}^{T}(\mathbf p_B-\mathbf t_{BT}),\qquad
\mathbf t_{TB}=-R_{BT}^{T}\mathbf t_{BT}.
$$

Noutra pose, T roda +90° em torno do eixo Z comum, mantendo a translação (0.1 m, 0 m) em B. A origem de B expressa em T passa a (0 m, +0.1 m), **não** (−0.1 m, 0 m). As mesmas matrizes transformam um ponto (0 m, 0.05 m) de T para B:

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

Referenciais e transformações **descrevem coordenadas**, não comandam motores. Em ROS 2, as translações usam convencionalmente metros; a [lição de referenciais](04-coordinate-frames.md#section-3) utiliza milímetros e exige conversão antes de combinar exemplos. Transformações estáticas descrevem montagens fixas; as dinâmicas são publicadas por componentes que obtêm estados atualizados. Para medições históricas usar o respetivo timestamp e tratar dados em falta.

<a id="section-8"></a>

## 8. URDF e robot_state_publisher

**Problema:** descrever uma estrutura mecânica partilhada. URDF contém links, joints, origens, eixos e propriedades opcionais visual, collision e inertial. robot_state_publisher combina URDF com posições de juntas, tipicamente sensor_msgs/msg/JointState em /joint_states, para publicar transforms. URDF não lê encoders nem fornece simulação ou IK. Usar unidades e convenções coerentes, normalmente m e rad.

**Origem das transformações:** URDF descreve joints `fixed` e móveis. `robot_state_publisher` publica transformações `static` para juntas fixas e utiliza posições em `/joint_states` (`sensor_msgs/msg/JointState`) para produzir transformações `dynamic` de joints móveis. O URDF **não mede** posições articulares nem recria medições em falta. Dimensões em metros, ângulos em radianos e timestamps devem ser coerentes.

<a id="section-9"></a>

## 9. ros2_control e fronteira do hardware

**Problema:** separar algoritmos de drivers. ros2_control inclui controller manager, interfaces de estado (posição/velocidade), interfaces de comando (posição/velocidade/effort) e abstrações de hardware. Planeador → controlador → interface → dispositivo, com feedback de estado. Receber uma mensagem ROS não garante timing de tempo real, limites de corrente ou paragem segura. Este laboratório não controla atuadores.

[First-order dynamics](02-first-order-dynamics.md) · [Feedback PID](03-feedback-control.md)

**Papel do gestor de controladores:** `controller_manager` gere o ciclo de vida dos controladores e, através do gestor de recursos, o acesso às interfaces de estado (state interfaces) e de comando (command interfaces). Um controlador pode ler um estado medido, como o exemplo hipotético `joint1/position`; um controlador ativo pode reservar uma interface de comando compatível para escrever uma referência. O valor medido não é a referência e dois controladores não podem reservar livremente a mesma interface de comando já ocupada. Ativação e gestão de recursos não equivalem à descoberta de topics.

**Limite deste laboratório:** `/training/status` e `/training/count` demonstram um topic e um service, **não `ros2_control`**. Nenhum dos dois nodes é um controlador e o laboratório não executa `controller_manager`, interfaces de hardware ou controlo em malha fechada. Um smoke test bem-sucedido não valida o ciclo de vida dos controladores, os tempos de controlo ou a segurança dos dispositivos. Ver [introdução oficial ao ros2_control](https://control.ros.org/jazzy/doc/getting_started/getting_started.html).

**Prática: ros2_control e TF2 sem GUI com junta virtual:** [Prática: ros2_control e TF2 sem GUI com junta virtual](07-ros2-control-lab.md). O novo laboratório explica URDF, GenericSystem, comandos, estados, /joint_states, TF2, QoS e diagnóstico do loader ARM64; não controla equipamento real.

**Próximo passo: arquitetura completa.** O [diagrama Mermaid ROS 2 de cinco etapas](08-ros2-robot-architecture.md) liga perceção, TF2 temporal, planeamento, controlo e realimentação. A parte de equipamento real é conceptual.

<a id="section-10"></a>

## 10. QoS, DDS discovery e Docker

**Problema:** diagnosticar perdas e componentes invisíveis. QoS inclui reliable/best_effort, volatile/transient_local, history e depth. Um subscriber com exigências incompatíveis pode ficar sem mensagens apesar de nome e tipo iguais. DDS usa normalmente multicast UDP e portas dinâmicas; Docker Desktop, VPN e firewall complicam discovery. ROS_DOMAIN_ID deve coincidir. Tudo corre num único contentor sem privilégios nem portas do host; não testa vários hosts.

**Exemplo de QoS incompatível:** um publisher oferece `best_effort`, mas um subscriber exige `reliable`. Mesmo com o nome e tipo do topic corretos e endpoints visíveis, o subscriber **não recebe mensagens** porque pede uma garantia que não está disponível. No sentido inverso, um subscriber `best_effort` pode receber de um publisher `reliable` se as restantes políticas QoS forem compatíveis. `volatile` não reproduz mensagens antigas; `transient_local` pode reter um histórico limitado enquanto o publisher compatível estiver disponível, **não é um registo distribuído persistente**.

**Diagnóstico por ordem:** verificar `ROS_DOMAIN_ID=42` dentro do mesmo contentor, executar `ros2 node list`, `ros2 topic info /training/status -v` para endpoints e QoS e `docker compose logs demo` para verificar processos. Se o grafo continuar invisível, investigar RMW/DDS, interfaces de rede e firewall. Expor portas TCP não resolve genericamente DDS; comunicação entre computadores não foi testada.

[Documentação oficial de QoS no ROS 2 Jazzy](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)

[Alternativa: imagem ROS oficial sem Compose nem Dockerfile próprio](../../../ros2/PLAIN_DOCKER.md)

<a id="section-11"></a>

## 11. Prática: dois nodes, topic, service e launch

docker compose up --build -d inicia o exemplo. Os logs devem mostrar samples enviados e recebidos, com contagem crescente. O service responde com success=True e uma mensagem como received 12 samples; o valor depende do tempo de execução. Um [smoke test Docker separado no GitHub Actions](../../../.github/workflows/ros2-live-smoke.yml) **executou a aplicação num único contentor** e verificou os dois nós ROS, uma mensagem tipada em `/training/status` e a resposta do serviço `/training/count`. A validação normal não executa ROS. Estes testes não comprovam DDS entre computadores, tempos determinísticos, equipamento real ou o Docker local do leitor.

[Complete source, expected results and diagnostics](../../../ros2/README.md). From the repository root:

Para estudar por etapas, comece pelo talker `demo_nodes_cpp` e o listener `demo_nodes_py` instalados na imagem; depois examine o pacote próprio `telemetry_demo` e só então `ros2_control`. O Dockerfile instala os demos pelo APT e compila `telemetry_demo` com `colcon`. Abra **um shell Bash interativo** e carregue os ambientes **uma vez por shell novo**: outro `docker compose exec` não herda o ambiente do `CMD`.

No host, inicie o container e abra um shell interativo:

```bash
cd ros2
docker compose up --build -d
docker compose logs --tail=20 demo
docker compose exec demo bash
```

Dentro do container, e não no host, carregue os ambientes uma vez e veja o grafo:

```bash
echo "$ROS_DISTRO"
ros2 node list
ros2 service call /training/count std_srvs/srv/Trigger "{}"
exit
```

Depois de `exit`, no host, encerre a execução:

```bash
docker compose down
```

**Limite de confiança do CI:** o teste Docker real do ROS 2 é agora executado automaticamente apenas depois de alterações chegarem a `main`, ou através de `workflow_dispatch` em `main`. Não é executado para revisões `pull_request`, pois isso faria com que o runner anfitrião executasse scripts Bash e Dockerfiles fornecidos pelo PR. Os testes Python isolados antes da integração não substituem um teste ROS real. As alterações exigem revisão independente antes de integrar e verificação do teste live depois.

<a id="section-12"></a>

## 12. Glossário e limites

- **Node / processo:** um node é um componente lógico ROS com nome; um processo do sistema pode conter vários nodes.
- **ROS graph:** conjunto de endpoints atualmente descobertos, não um registo central permanente nem uma autorização.
- **Topic:** fluxo assíncrono com nome, que pode ter vários publishers e subscribers.
- **Message:** estrutura tipada definida por uma interface ROS, não um objeto Python ou C++ arbitrário.
- **Publisher / subscriber:** emissor e recetor de mensagens; discovery e QoS compatível são necessários para a entrega.
- **Service:** pedido/resposta tipados para uma interação curta; um timeout não prova que o servidor nada executou.
- **Action:** objetivo com feedback, resultado e pedido de cancelamento; cancelar não garante paragem imediata.
- **Parameter:** valor pertencente a um node; alterá-lo não reconfigura automaticamente um temporizador em execução.
- **RMW / DDS:** RMW abstrai o middleware; DDS é tecnologia comum de discovery e transporte, não autenticação por si só.
- **colcon / ament:** orquestração da construção do workspace / integração dos pacotes ROS, não transporte de mensagens.
- **Launch:** descrição dos processos e configuração a iniciar; arranque não implica prontidão.
- **tf2:** infraestrutura de transformações de referenciais com timestamps, não um solver de cinemática inversa.
- **URDF / robot_state_publisher:** modelo estrutural do robô / publicação de transformações a partir do modelo e estados das articulações.
- **ros2_control:** ciclo de vida de controladores e interfaces state/command geridas; ausente do laboratório topic/service.
- **QoS:** compatibilidade e políticas de entrega e histórico, não um registo persistente nem certificação de segurança.

**Versões verificadas em 13 de novembro de 2026:** ROS 2 Jazzy LTS tem suporte até maio de 2029 e Lyrical LTS até maio de 2031. A tag Docker não fixa um digest imutável da imagem nem versões dos pacotes apt.

**Primary sources:** [ROS 2 releases](https://github.com/ros2/ros2_documentation/blob/rolling/source/Releases.rst) · [Jazzy documentation](https://docs.ros.org/en/jazzy/) · [tf2](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html) · [URDF](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/URDF/URDF-Main.html) · [ros2_control](https://control.ros.org/jazzy/)
