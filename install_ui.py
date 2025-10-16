
import os, sys, re, pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parent
PROJECT_ROOT = pathlib.Path.cwd()

def find_file(start: pathlib.Path, name: str):
    # Find the FIRST occurrence of a file matching 'name'
    for p in start.rglob(name):
        return p
    return None

def ensure_installed_app(settings_path: pathlib.Path, app_name="ui"):
    txt = settings_path.read_text(encoding="utf-8")
    if "INSTALLED_APPS" not in txt:
        raise SystemExit("[ERRO] Não encontrei INSTALLED_APPS em settings.py")

    if re.search(rf"['\"]{app_name}['\"]", txt):
        print(f"[OK] '{app_name}' já está em INSTALLED_APPS.")
        return

    # Try to insert inside the list
    def repl(m):
        inner = m.group(1)
        # ensure trailing comma
        if inner.strip() and not inner.strip().endswith(","):
            inner = inner + ","
        return f"INSTALLED_APPS = [{inner}\n    \"{app_name}\",\n]"

    new_txt, n = re.subn(r"INSTALLED_APPS\s*=\s*\[(.*?)\]", repl, txt, flags=re.S)
    if n == 0:
        # Fallback: append near rest_framework/estudos
        new_txt = txt.replace("\"estudos\",", "\"estudos\",\n    \"ui\",")
    settings_path.write_text(new_txt, encoding="utf-8")
    print(f"[OK] '{app_name}' adicionado a INSTALLED_APPS.")

def ensure_urls(urls_path: pathlib.Path):
    txt = urls_path.read_text(encoding="utf-8")
    changed = False

    # Ensure imports
    if "from django.urls import path, include" not in txt:
        if "from django.urls import path" in txt:
            txt = txt.replace("from django.urls import path", "from django.urls import path, include")
            changed = True
        else:
            txt = "from django.urls import path, include\n" + txt
            changed = True

    def ensure_pattern(snippet, line_to_add):
        nonlocal txt, changed
        if snippet not in txt:
            txt = re.sub(r"urlpatterns\s*=\s*\[\s*", lambda m: m.group(0) + f"{line_to_add}\n    ", txt, flags=re.S)
            changed = True

    ensure_pattern('include("django.contrib.auth.urls")', 'path("accounts/", include("django.contrib.auth.urls")),' )
    ensure_pattern('include("estudos.urls")',            'path("api/", include("estudos.urls")),'                  )
    ensure_pattern('include("ui.urls")',                 'path("", include("ui.urls")),'                           )

    if changed:
        urls_path.write_text(txt, encoding="utf-8")
        print("[OK] main/urls.py atualizado.")
    else:
        print("[OK] main/urls.py já possuía as rotas necessárias.")

def main():
    print(">> Instalador do app 'ui'")
    # Look for main/settings.py and main/urls.py
    main_settings = find_file(PROJECT_ROOT, "settings.py")
    main_urls = find_file(PROJECT_ROOT, "urls.py")

    if not main_settings or "main" not in str(main_settings):
        print("[ERRO] Não encontrei main/settings.py. Execute este script na RAIZ do projeto (onde está manage.py).")
        sys.exit(1)
    if not main_urls or "main" not in str(main_urls):
        print("[ERRO] Não encontrei main/urls.py. Execute este script na RAIZ do projeto (onde está manage.py).")
        sys.exit(1)

    print(f"[INFO] settings.py: {main_settings}")
    print(f"[INFO] urls.py: {main_urls}")

    # Copy ui folder if not already present
    src_ui = ROOT / "ui"
    dst_ui = PROJECT_ROOT / "ui"
    if not dst_ui.exists():
        shutil.copytree(src_ui, dst_ui)
        print(f"[OK] Copiei 'ui/' para {dst_ui}")
    else:
        print("[OK] 'ui/' já existe no projeto.")

    ensure_installed_app(main_settings, "ui")
    ensure_urls(main_urls)

    print("\nTudo pronto! Agora rode:")
    print("  python manage.py migrate")
    print("  python manage.py createsuperuser  (se necessário)")
    print("  python manage.py runserver")
    print("\nDepois acesse: /accounts/login/ e /")

if __name__ == '__main__':
    main()
