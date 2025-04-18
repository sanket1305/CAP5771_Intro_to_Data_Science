def generate_ner_tags(text: str, entities: list[tuple[int, int, str]]) -> list[str]:
    text = text.split()
    entities.sort()
    res = ["O"]*len(text)

    for start, end, entity_name in entities:
      idx = 0
      is_first_word = True
      for word_idx in range(len(text)):
        word = text[word_idx]
        word_b = idx
        word_e = idx + len(word)

        if word_b < end and word_e > start:
          if is_first_word:
            res[word_idx] = "B-" + entity_name
            is_first_word = False
          else:
            res[word_idx] = "I-" + entity_name
        idx += len(word) + 1
    
    return res

print(generate_ner_tags("Barack Obama was born in Hawaii.", [(0, 12, "PERSON"), (25, 31, "LOCATION")]))