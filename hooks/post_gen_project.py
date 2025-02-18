def remove_disabled_components():
    import shutil
    from pathlib import Path
    allowed_components = {
        "table": "{{ cookiecutter.components.table }}",
        "chart": "{{ cookiecutter.components.chart }}",
        "map": "{{ cookiecutter.components.map }}"
    }

    def is_allowed_dir(dir_name):
        for comp, enabled in allowed_components.items():
            if enabled and comp in dir_name.lower():
                return True
        return False

    components_folder = Path("{{ cookiecutter.project_slug }}", "src", "components")
    if components_folder.exists():
        for component_dir in components_folder.iterdir():
            if component_dir.is_dir() and not is_allowed_dir(component_dir.name):
                shutil.rmtree(component_dir)
                print(f"Removed component folder: {component_dir}")

def main():
    # Remove component folders that are not enabled in cookiecutter.json
    remove_disabled_components()

    print("Project initialized, keep up the good work!")  # noqa: F821

if __name__ == "__main__":
    main()
