import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# secrets.json 파일에서 API 키, SQL URL 등 민감한 정보 가져오기
def get_secret(key: str, json_path: str = str(BASE_DIR / "secrets.json")):
    with open(json_path) as f:
        secrets = json.loads(f.read())
        try:
            return secrets[key]
        except KeyError:
            raise EnvironmentError(f"{key}가 존재하지 않습니다.")


if __name__ == "__main__":
    print(BASE_DIR)
