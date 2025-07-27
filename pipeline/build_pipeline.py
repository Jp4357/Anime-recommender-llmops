from src.data_loader import AnimeDataLoader
from src.vectore_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException


logger = get_logger(__name__)


def main():
    try:

        logger.info("Starting the build pipeline...")

        data_loader = AnimeDataLoader(
            original_csv="data/anime_with_synopsis.csv",
            processed_csv="data/anime_updated.csv",
        )

        processed_csv = data_loader.load_and_process()

        vector_builder = VectorStoreBuilder(csv_path=processed_csv)

        vector_builder.build_and_save_vector_store()

        logger.info("Vector store Built successfully.")

        logger.info("Build pipeline completed successfully.")

    except Exception as e:
        logger.error(f"Failed to execute build pipeline: {str(e)}")
        raise CustomException("Error during build pipeline.", e)


if __name__ == "__main__":
    main()
