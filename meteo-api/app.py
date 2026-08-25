releves = [
    {"ville": "Paris", "temperature": 21},
    {"ville": "Lyon", "temperature": 26},
    {"ville": "Marseille", "temperature": 26},
]

def moyenne():
    return sum(r["temperature"] for r in releves) / len(releves)

if __name__ == "__main__":
    print("Temperature moyenne :", moyenne())
