import base64
import json

def main():
    lazy_load_resource = {}
    with open("datalist.json", "r") as fp:
        targets = json.loads(fp.read())
    for target in targets:
        with open(target["file"], "rb") as fp:
            data = base64.b64encode(fp.read())
            lazy_load_resource[target["key"]] = {
                "scale": target["scale"],
                "y": target["y"],
                "rotate": target["rotate"],
                "glb": data.decode("utf-8")
            }

    with open("../website/polygon.json", "w") as fp:
        fp.write(json.dumps(lazy_load_resource))

main()