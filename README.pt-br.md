# **RapidClip**

**RapidClip** é um projeto em andamento que busca automatizar a criação de vídeos curtos, ideais para plataformas como YouTube Shorts, Instagram Reels, TikTok e Kwai. O objetivo é permitir que o sistema gere vídeos completos a partir de um tema fornecido, combinando narração, música de fundo, imagens dinâmicas, efeitos visuais, legendas sincronizadas e registro detalhado do processo.

🇺🇸 Para a versão em inglês deste README, veja [README.md](README.md).

---

## **Funcionalidades Implementadas**

- **Criação Automática de Conteúdo**: Gerar roteiros personalizados com base no tema fornecido.
- **Narração de Áudio**: Transformar o roteiro em narração de alta qualidade, com suporte tanto ao ElevenLabs quanto ao OpenAI TTS.
- **Reprocessamento de Áudio**: Reprocessar áudios que excedam uma duração especificada, garantindo compatibilidade com as restrições das plataformas.
- **Geração de Legendas**: Gerar legendas com alinhamento e segmentação aprimorados:
  - Tokeniza o texto transcrito, preservando a pontuação.
  - Alinha palavras com seus respectivos timestamps e pontuações.
  - Cria legendas legíveis e sincronizadas, com limites de caracteres e palavras por linha.
- **Geração de Imagens Aprimorada**:
  - Gerar prompts diversificados para criação de imagens, utilizando o contexto completo das legendas e os prompts gerados anteriormente (quando disponíveis), assegurando variação e criatividade.
  - Suporte à configuração da versão do modelo SANA via variável de ambiente.
- **Suporte a Múltiplos Idiomas**: Permitir a criação de conteúdo, narração e legendas em diversos idiomas.
- **Registro de Processo**: Salvar logs detalhados do andamento do processo – incluindo os prompts gerados para cada intervalo de imagem – na pasta de saída de cada vídeo.

---

## **Funcionalidades Planejadas**

- **Integração de Música de Fundo**: Selecionar trilhas sonoras locais para enriquecer o vídeo.
- **Imagens Relevantes**: Aperfeiçoar a seleção de imagens para ilustrar o conteúdo.
- **Efeitos Visuais e Transições**: Aplicar zoom, animações e cortes suaves.
- **Renderização Completa**: Criar o vídeo final pronto para publicação.

---

## **Como Usar**

Antes de executar o RapidClip, certifique-se de configurar as variáveis de ambiente necessárias. Utilize o arquivo `.env.example` como modelo e crie um arquivo `.env` com as seguintes variáveis:

```plaintext
OPENAI_API_KEY=your-openai-api-key
ELEVENLABS_API_KEY=your-elevenlabs-api-key
REPLICATE_API_TOKEN=your-replicate-api-token
SANA_MODEL_VERSION=your-sana-model-version
```

Após configurar as variáveis, você pode executar o RapidClip utilizando um dos comandos abaixo.

### Exemplo com ElevenLabs TTS

```bash
python src/main.py --theme "Curiosidades da História (uma única curiosidade)" \
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

#### Abordagem para Legendas:
O processo de geração de legendas garante alinhamento e legibilidade aprimorados:
- **Tokenização com Pontuação**: O texto completo transcrito é tokenizado em palavras e pontuações, preservando a ordem original.
- **Alinhamento de Palavras e Pontuação**: Cada palavra é alinhada com seu token correspondente, garantindo que a pontuação esteja corretamente posicionada.
- **Segmentação de Cues**: As legendas são divididas em segmentos menores (cues) com base em limites de palavras e caracteres por linha, mantendo a sincronização com os timestamps do áudio.

---

## **Status do Projeto**

**RapidClip** está em sua fase inicial de desenvolvimento. As funcionalidades principais estão implementadas e testadas. Atualizações recentes incluem:
- Melhoria na geração de prompts para imagens, com diversificação e inclusão condicional dos prompts anteriores.
- Suporte à configuração da versão do modelo SANA via variável de ambiente.
- Inclusão de registro detalhado do processo, com logs salvos em cada pasta de saída de vídeo.

---

## **Próximos Passos**

1. Estruturar o pipeline para criação de roteiros, narração e geração de imagens.
2. Implementar efeitos visuais e transições entre imagens.
3. Garantir a sincronização precisa entre áudio, imagens e legendas.
4. Otimizar a renderização final para compatibilidade com plataformas de vídeos curtos.
5. Expandir o suporte ao processamento de áudio, incluindo reprocessamento de arquivos longos e gerenciamento de limites definidos pelo usuário.

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