"""
Client program
"""

from serveapi import interface as itfc


if __name__ == "__main__":
    transformers = itfc.DynamicModule("transformers")
    cap = transformers.pipeline(model="ydshieh/vit-gpt2-coco-en")
    print(cap)
    x = "https://images.unsplash.com/photo-1582979512210-99b6a53386f9?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    tmp = cap(x)
    print(tmp)

    np = itfc.DynamicModule("np")
    resp = np.linalg.norm([100, 200, 300])
    print(resp)
