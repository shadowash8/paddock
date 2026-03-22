# paddock

a random F1 quote or meme terminal ASCII art generator.

eg.

```
❯ paddock

                  _____            __       __             __
                 / __(_)_ _  ___  / /_ __  / /__ _  _____ / /_ __
                _\ \/ /  ' \/ _ \/ / // / / / _ \ |/ / -_) / // /
               /___/_/_/_/_/ .__/_/\_, / /_/\___/___/\__/_/\_, /
                          /_/     /___/                   /___/


    — Du Du Du Max Verstappen

```

## requirement

- python

## installation

### aur

if you are on archlinux you can install the `paddock-git` package with your aur helper.

```bash
paru -S paddock-git
```

### everywhere else

```bash
pipx install git+https://github.com/shadowash8/paddock.git
```

## development

```bash
git clone https://github.com/shadowash8/paddock.git
cd paddock

python -m venv .venv
source .venv/bin/activate

pip install .
```
