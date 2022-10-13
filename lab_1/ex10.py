def words_in_text(text):
    """Count how many words are in a text."""
    words = text.split()
    return len(words)

def main():
    print(words_in_text("I have Python exam tomorrow"))

if __name__ == "__main__":
    main()