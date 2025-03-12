# **RapidClip**

**RapidClip** é um projeto que automatiza a criação de vídeos curtos, ideais para plataformas como YouTube Shorts, Instagram Reels, TikTok e Kwai. A versão atual permite gerar vídeos completos a partir de um tema fornecido, combinando narração, música de fundo, imagens dinâmicas, efeitos visuais, legendas sincronizadas, registro detalhado do processo e montagem final do vídeo com transições animadas.

🇺🇸 Para a versão em inglês deste README, veja [README.md](README.md).

---

## **Funcionalidades Implementadas**

- **Criação Automática de Conteúdo**: Geração de roteiros personalizados com base no tema fornecido.
- **Narração de Áudio**: Transformação do roteiro em narração de alta qualidade, com suporte tanto ao ElevenLabs quanto ao OpenAI TTS.
- **Reprocessamento de Áudio**: Reprocessamento de áudios que excedem uma duração especificada, garantindo compatibilidade com as restrições das plataformas.
- **Geração de Legendas**: Criação de legendas com melhor alinhamento e segmentação:
  - Tokenização do texto transcrito, preservando a pontuação.
  - Alinhamento das palavras com seus respectivos timestamps e pontuações.
  - Criação de legendas legíveis e sincronizadas, com limites de caracteres e palavras por linha.
- **Geração de Imagens Aprimorada**:
  - Geração de prompts diversificados para criação de imagens, utilizando o contexto completo das legendas e os prompts gerados anteriormente (quando disponíveis), assegurando variação e criatividade.
  - Suporte à configuração da versão do modelo SANA via variável de ambiente.
- **Montagem Final do Vídeo**: Composição do vídeo final utilizando o áudio, as imagens geradas e as legendas, com transições animadas (incluindo um efeito de zoom in lento nas imagens) e mantendo a resolução de 1080x1920. O primeiro frame do vídeo é a primeira imagem gerada.
- **Suporte a Múltiplos Idiomas**: Possibilidade de criação de conteúdo, narração e legendas em diversos idiomas.
- **Registro de Processo**: Armazenamento de logs detalhados do andamento do processo – incluindo os prompts gerados para cada intervalo de imagem – na pasta de saída de cada vídeo.

---

## **Funcionalidades Planejadas**

- **Integração de Música de Fundo**: Seleção de trilhas sonoras locais para enriquecer o vídeo.
- **Imagens Relevantes**: Aperfeiçoamento na seleção de imagens para ilustrar melhor o conteúdo.
- **Efeitos Visuais e Transições**: Aplicação de zoom, animações e cortes suaves adicionais.
- **Renderização Completa**: Criação do vídeo final pronto para publicação.
- **Recursos Avançados de Edição de Vídeo**: Expansão das capacidades de montagem e edição para funcionalidades mais avançadas.

---

## **Como Usar**

Antes de executar o RapidClip, configure as variáveis de ambiente necessárias. Utilize o arquivo `.env.example` como modelo e crie um arquivo `.env` com as seguintes variáveis:

```plaintext
OPENAI_API_KEY=your-openai-api-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key
REPLICATE_API_TOKEN=your-replicate-api-token
SANA_MODEL_VERSION=your-sana-model-version
```

Após configurar as variáveis, execute o RapidClip utilizando um dos comandos abaixo.

### Exemplo com ElevenLabs TTS

```bash
python src/main.py --theme "Curiosidades do Espaço (uma única curiosidade)" \
  --language "pt-BR" \
  --voice_id "CstacWqMhJQlnfLPxRG4" \
  --max_duration 60 \
  --tts_service elevenlabs
```

### Exemplo com OpenAI TTS

```bash
python src/main.py --theme "Curiosidades da Tecnologia (uma única curiosidade)" \
  --language "pt-BR" \
  --max_duration 60 \
  --tts_service openai \
  --openai_tts_model "tts-1-hd" \
  --openai_tts_voice "alloy"
```

### Parâmetros:
- `--theme`: O tema do roteiro a ser criado.
- `--language`: O idioma do roteiro e da narração.
- `--tts_service`: O serviço de TTS a ser utilizado (`elevenlabs` ou `openai`). O padrão é `elevenlabs`.
- `--voice_id`: O ID da voz a ser utilizada para a narração (obrigatório para ElevenLabs).
- `--openai_tts_model`: O modelo de TTS da OpenAI a ser utilizado (padrão: `tts-1-hd`).
- `--openai_tts_voice`: A voz da OpenAI a ser utilizada (padrão: `alloy`).
- `--max_duration`: A duração máxima permitida para o áudio (em segundos).

### Saída:
Os arquivos gerados serão salvos na pasta `output/`, incluindo:
- Um arquivo de áudio (`.mp3`) com a narração.
- Um arquivo de legendas (`.srt`) sincronizado com o áudio.
- Um arquivo `process.log` contendo logs detalhados do andamento do processo, inclusive os prompts gerados para cada intervalo de imagem.
- Um vídeo final (`_final.mp4`) montado com transições animadas, mantendo a resolução de 1080x1920.

#### Abordagem para Legendas:
O processo de geração de legendas garante melhor alinhamento e legibilidade:
- **Tokenização com Pontuação**: O texto completo transcrito é tokenizado em palavras e pontuações, preservando a ordem original.
- **Alinhamento de Palavras e Pontuação**: Cada palavra é alinhada com seu token correspondente, garantindo que a pontuação seja posicionada corretamente.
- **Segmentação de Cues**: As legendas são divididas em segmentos menores (cues) com base em limites de palavras e caracteres por linha, mantendo a sincronização com os timestamps do áudio.

---

## **Status do Projeto**

**RapidClip** está consolidado em sua versão atual. As funcionalidades principais foram implementadas e testadas, incluindo:
- Geração de roteiros, narração, legendas, e imagens com prompts diversificados.
- Montagem final do vídeo com transições animadas e efeito de zoom in nas imagens.
- Registro detalhado do processo com logs salvos na pasta de saída de cada vídeo.
- Suporte à configuração da versão do modelo SANA via variável de ambiente.

Apesar da versão atual estar consolidada, os seguintes planos futuros permanecem:

- **Integração de Música de Fundo**: Selecionar trilhas sonoras locais para enriquecer o vídeo.
- **Imagens Relevantes**: Aperfeiçoar a seleção de imagens para ilustrar melhor o conteúdo.
- **Efeitos Visuais e Transições**: Aplicar zoom, animações e cortes suaves adicionais.
- **Renderização Completa**: Otimizar o vídeo final para compatibilidade com plataformas de vídeos curtos.
- **Recursos Avançados de Edição de Vídeo**: Expandir as capacidades de montagem e edição para funcionalidades mais avançadas.
- **Suporte Avançado ao Processamento de Áudio**: Incluir reprocessamento de arquivos longos e gerenciamento de limites definidos pelo usuário.

---

## **Contribuições**

Estamos abertos a contribuições! Caso deseje colaborar com o projeto, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade ou correção de bug:
   ```bash
   git checkout -b minha-contribuicao
   ```
3. Realize suas alterações e envie um pull request detalhando suas modificações.

Contamos com sua ajuda para tornar o RapidClip ainda melhor!

---

## **Licença**

Este projeto está licenciado sob a licença **MIT**. Isso significa que você pode usá-lo, modificá-lo e distribuí-lo, desde que a licença original seja incluída no código. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.