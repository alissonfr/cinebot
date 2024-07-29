import json
from typing import List, Dict

def read_files(files: List[str]) -> List[Dict[str, str]]:
    convos = []
    for convo in files:
        try:
            with open(convo, "r", encoding="utf-8") as f:
                convos.extend(json.load(f))
        except FileNotFoundError:
            print(f"Arquivo não encontrado: {convo}")
        except json.JSONDecodeError:
            print(f"Erro de decodificação JSON em: {convo}")
        except Exception as e:
            print(f"Erro inesperado ao carregar {convo}: {e}")
    return convos
