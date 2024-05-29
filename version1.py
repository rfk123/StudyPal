from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('./OS.pdf')
pages = loader.load_and_split()

print(pages[3].page_content)
