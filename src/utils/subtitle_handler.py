import re


def seconds_to_srt_timestamp(seconds: float) -> str:
    """
    Converts seconds to the SRT timestamp format (HH:MM:SS,ms).

    Args:
        seconds (float): The time in seconds to be converted.

    Returns:
        str: The formatted timestamp as a string in SRT format.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    milliseconds = int((seconds - int(seconds)) * 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def tokenize_with_punctuation(text: str):
    """
    Tokenizes a text into words and punctuation marks, preserving their order.

    Args:
        text (str): The text to tokenize.

    Returns:
        list[str]: A list of tokens, where words and punctuation marks are separate.
    """
    # Extracts alphanumeric sequences (words) and punctuation marks as separate tokens.
    # \w+ extracts words; [^\w\s]+ extracts punctuation; the order in the text is preserved.
    return re.findall(r"\w+|[^\w\s]+", text)


def align_words_with_punctuation(words, full_text):
    """
    Aligns a list of word objects with the punctuated tokens from the full text.

    Args:
        words (list): A list of word objects, each containing `word`, `start`, and `end`.
        full_text (str): The full transcript text with punctuation.

    Returns:
        list[tuple]: A list of tuples where each tuple contains (start, end, word_with_punctuation).
    """
    punct_tokens = tokenize_with_punctuation(full_text)
    aligned_words = []

    # Index to traverse punct_tokens
    pt_idx = 0

    for w_obj in words:
        # Search for the next alphanumeric token that matches a word.
        # Assume that the order of words in `words` matches the order in the full text.
        base_word = None
        while pt_idx < len(punct_tokens):
            token = punct_tokens[pt_idx]
            pt_idx += 1
            # Check if the token is a word (alphanumeric)
            if re.match(r"\w+", token, flags=re.UNICODE):
                # Found the corresponding word
                # In this example, assume the order is correct.
                base_word = token
                # Check if the next token is punctuation
                if pt_idx < len(punct_tokens):
                    next_token = punct_tokens[pt_idx]
                    if re.match(r"[^\w\s]+", next_token):
                        # Attach punctuation to the current word
                        base_word += next_token
                        pt_idx += 1
                # Final assembled word
                break

        if base_word is None:
            # If no matching token is found (unlikely), use the original word
            base_word = w_obj.word

        # Create a new word object with the punctuated word
        # Keep the same start and end times, only adjust the "word"
        aligned_words.append((w_obj.start, w_obj.end, base_word))

    return aligned_words


def format_srt_from_aligned_words(aligned_words, max_words_per_cue=10, max_chars_per_cue=40):
    """
    Formats a list of aligned words into SRT subtitle format.

    Args:
        aligned_words (list[tuple]): A list of tuples containing (start, end, word_with_punctuation).
        max_words_per_cue (int): Maximum number of words allowed per subtitle cue.
        max_chars_per_cue (int): Maximum number of characters allowed per subtitle cue.

    Returns:
        str: The SRT-formatted subtitle text.
    """
    cues = []
    current_words = []

    def flush_cue():
        """
        Flushes the current buffered words into a subtitle cue.
        """
        if not current_words:
            return
        start_time = current_words[0][0]
        end_time = current_words[-1][1]
        # Build the cue text
        cue_text = " ".join(w[2] for w in current_words)
        cues.append((start_time, end_time, cue_text))

    for w_data in aligned_words:
        start, end, w_text = w_data
        # Check limits
        tentative_line = " ".join([cw[2] for cw in current_words] + [w_text])
        if (len(current_words) + 1 > max_words_per_cue) or (len(tentative_line) > max_chars_per_cue):
            flush_cue()
            current_words = [w_data]
        else:
            current_words.append(w_data)

    # Final flush
    flush_cue()

    srt_content = ""
    for i, (start, end, text) in enumerate(cues, start=1):
        srt_content += (
            f"{i}\n"
            f"{seconds_to_srt_timestamp(
                start)} --> {seconds_to_srt_timestamp(end)}\n"
            f"{text}\n\n"
        )

    return srt_content
