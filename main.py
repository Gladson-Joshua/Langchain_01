import os

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    keys = ["OPENAI_API_KEY", "ANTHROPIC_API_KEY", "GOOGLE_API_KEY"]
    for key in keys:
        status = "set" if os.getenv(key) else "missing"
        print(f"{key}: {status}")


if __name__ == "__main__":
    main()
