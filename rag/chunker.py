from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(pages):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )

    chunks = []
    for page in pages:
        chunks.extend(splitter.split_text(page))

    return chunks

# hobby-session-2

# hobby-session-4

# hobby-session-12

# hobby-session-13

# hobby-session-8

# hobby-session-21

# hobby-session-24

# hobby-session-5-1

# hobby-session-10-1

# hobby-session-13-1

# hobby-session-21-2

# hobby-session-25-1
