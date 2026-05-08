## Passo a passo

1. Clone o repositório:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Suba o ambiente com Docker Compose:
   ```bash
   docker compose up --build
   ```

3. Acesse o n8n no navegador:
   ```text
   http://localhost:5678
   ```

4. Importe o workflow do projeto:
   - Abra o n8n.
   - Clique em **Import from File**.
   - Selecione `n8n/workflow.json`.

5. Execute o workflow.

6. O script Python será executado dentro do container pelo nó **Execute Command**.

7. O arquivo de saída será salvo em:
   ```text
   /files/saida/resultado.json
   ```

8. No nó **Read/Write Files from Disk**, use este caminho:
   ```text
   /files/saida/resultado.json
   ```

9. No nó **Extract From File**, extraia o conteúdo JSON para uso no fluxo.

10. Para encerrar o ambiente, execute:
   ```bash
   docker compose down
   ```

## Observações

- Não use caminhos locais do seu computador, como `/media/usuario/...`.
- Sempre use o caminho interno do container, que neste projeto é `/files/...`.
- Se o arquivo não aparecer, verifique se o script criou corretamente a pasta `saida/` e o arquivo `resultado.json`.