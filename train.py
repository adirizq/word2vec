from utils.preprocessors import Preprocessor

if __name__ == "__main__":
    pre = Preprocessor()

    txt_dataset_dir = "datasets\ind_wikipedia_2021_1M-sentences.txt"
    csv_dataset_dir = "datasets\Indonesian Sentiment Twitter Dataset Labeled.csv"
    conllu_dataset_dir = "datasets\id_gsd-ud-train.conllu"
    tsv_dataset_dir = "datasets\Indonesian_Manually_Tagged_Corpus_ID.tsv"

    pre.load_file(txt_dataset_dir, csv_dataset_dir, conllu_dataset_dir, tsv_dataset_dir)

    cleaned = pre.clean_sentence("Apakah ini adalah kalimat?")
    print(cleaned)