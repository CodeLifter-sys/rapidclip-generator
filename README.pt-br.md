# **RapidClip**

**RapidClip** é um projeto que automatiza a criação de vídeos curtos, ideais para plataformas como YouTube Shorts, Instagram Reels, TikTok e Kwai. A versão atual permite gerar vídeos completos a partir de um tema fornecido, combinando narração, imagens dinâmicas, efeitos visuais, legendas sincronizadas, registro detalhado do processo e montagem final do vídeo com transições animadas.

🇺🇸 Para a versão em inglês deste README, veja [README.md](README.md).

---

## **Vídeos de Demonstração gerados pelo RapidClip:**

<table>
  <thead>
    <tr>
      <th align="center"><g-emoji alias="arrow_forward">▶️</g-emoji> Demonstração 1</th>
      <th align="center"><g-emoji alias="arrow_forward">▶️</g-emoji> Demonstração 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center">
        <video controls width="480">
          <source src="https://raw.githubusercontent.com/itallonardi/rapidclip-generator/main/demos/pt-br/espaco.mp4" type="video/mp4">
          Seu navegador não suporta o elemento de vídeo.
        </video>
        <br>
        <a href="https://raw.githubusercontent.com/itallonardi/rapidclip-generator/main/demos/pt-br/espaco.mp4" download>Baixar Demonstração 1</a>
      </td>
      <td align="center">
        <video controls width="480">
          <source src="https://raw.githubusercontent.com/itallonardi/rapidclip-generator/main/demos/pt-br/tecnologia.mp4" type="video/mp4">
          Seu navegador não suporta o elemento de vídeo.
        </video>
        <br>
        <a href="https://raw.githubusercontent.com/itallonardi/rapidclip-generator/main/demos/pt-br/tecnologia.mp4" download>Baixar Demonstração 2</a>
      </td>
    </tr>
  </tbody>
</table>

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
- **Montagem Final do Vídeo**: Composição do vídeo final utilizando o áudio, as imagens geradas e as legendas, com transições animadas (incluindo efeito de zoom in) e mantendo a resolução de 1080x1920.
- **Imagens Relevantes**: Aperfeiçoamento na seleção de imagens para ilustrar melhor o conteúdo.
- **Efeitos Visuais e Transições**: Aplicação de zoom, animações e cortes suaves adicionais.
- **Renderização Completa**: Criação do vídeo final pronto para publicação.
- **Suporte a Múltiplos Idiomas**: Possibilidade de criação de conteúdo, narração e legendas em diversos idiomas.
- **Registro de Processo**: Armazenamento de logs detalhados do andamento do processo – incluindo os prompts gerados para cada intervalo de imagem – na pasta de saída de cada vídeo.

---

## **Funcionalidades Planejadas**

- **Integração de Música de Fundo**: Seleção de trilhas sonoras locais para enriquecer o vídeo.
- **Recursos Avançados de Edição de Vídeo**: Expansão das capacidades de montagem e edição para funcionalidades mais avançadas.

---

## **Como Usar o RapidClip**

Antes de utilizar o RapidClip, é necessário configurar as variáveis de ambiente. Utilize o arquivo `.env.example` como modelo para criar seu próprio arquivo `.env`, contendo as seguintes variáveis:

```plaintext
OPENAI_API_KEY=sua-chave-api-openai
ELEVENLABS_API_KEY=sua-chave-api-elevenlabs
REPLICATE_API_TOKEN=sua-chave-api-replicate
SANA_MODEL_VERSION=versao-do-modelo-sana
```

---

## **Execução do RapidClip**

### **Usando Docker**

Você pode executar o RapidClip via Docker, facilitando o uso em um ambiente isolado com todas as dependências pré-instaladas. Para mais detalhes, consulte o [README.DOCKER.md](README.DOCKER.md).

### **Execução local (sem Docker)**

Se preferir rodar o projeto diretamente na sua máquina, siga os passos abaixo:

**1. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**2. Gere o vídeo:**

**Usando ElevenLabs TTS:**
```bash
python src/main.py --theme "Curiosidades do Espaço (uma única curiosidade)" \
  --language "pt-BR" \
  --voice_id "CstacWqMhJQlnfLPxRG4" \
  --max_duration 60 \
  --tts_service elevenlabs
```

**Usando OpenAI TTS:**
```bash
python src/main.py --theme "Curiosidades da Tecnologia (uma única curiosidade)" \
  --language "pt-BR" \
  --max_duration 60 \
  --tts_service openai \
  --openai_tts_model "tts-1-hd" \
  --openai_tts_voice "onyx"
```

### **Parâmetros:**
- `--theme`: Tema do roteiro do vídeo.
- `--language`: Idioma do roteiro e da narração.
- `--tts_service`: Escolha entre `elevenlabs` (padrão) ou `openai`.
- `--voice_id`: Necessário ao utilizar ElevenLabs.
- `--openai_tts_model`: Modelo de TTS do OpenAI (padrão: `tts-1-hd`).
- `--openai_tts_voice`: Voz utilizada pelo OpenAI TTS (padrão: `alloy`).
- `--max_duration`: Duração máxima do áudio em segundos.

### **Arquivos gerados:**

Os arquivos gerados estarão disponíveis na pasta `output/`:
- **Áudio (`.mp3`)**: Arquivo com a narração.
- **Legendas (`.srt`)**: Legendas sincronizadas.
- **Logs (`process.log`)**: Registro detalhado do processo.
- **Vídeo final (`_final.mp4`)**: Vídeo renderizado com legendas e transições (resolução: 1080x1920).

### **Abordagem das legendas:**
- **Tokenização com pontuação**: Preserva a pontuação original.
- **Alinhamento de palavras e pontuação**: Assegura posicionamento correto das pontuações.
- **Segmentação em cues**: Legendas divididas em segmentos menores para melhor legibilidade e sincronização.

---

## **Status do Projeto**

**RapidClip** consolidou sua versão inicial. As funcionalidades principais foram implementadas e testadas, incluindo:
- Geração de roteiros, narração, legendas e imagens com prompts diversificados.
- Montagem final do vídeo com transições animadas e efeito de zoom in nas imagens.
- Aperfeiçoamento na seleção de imagens e aplicação de efeitos visuais.
- Registro detalhado do processo com logs salvos na pasta de saída de cada vídeo.
- Suporte à configuração da versão do modelo SANA via variável de ambiente.

---

## **Próximos Passos**

1. Implementar trilha sonora de fundo livre de direitos autorais.
2. Implementar recursos avançados de edição de vídeo para funcionalidades mais sofisticadas.

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