def remove_disabled_components():
    import shutil
    from pathlib import Path
    allowed_components = {
        "table": "{{ cookiecutter.components.table }}",
        "chart": "{{ cookiecutter.components.chart }}",
        "map": "{{ cookiecutter.components.map }}"
    }

    def is_allowed_dir(dir_name):
        # Convert directory name to lowercase for case-insensitive comparison
        dir_name = dir_name.lower()
        for comp, enabled in allowed_components.items():
            # Check if the directory name exactly matches the component name
            print(f"Checking {comp} in {dir_name}")
            print(f"Enabled: {enabled}")
            if enabled and dir_name == comp:
                return True
        return False

    components_folder = Path("src", "components")

    # Try to list parent directories to see if they exist
    parent = components_folder.parent
    grandparent = parent.parent

    if components_folder.exists():
        for component_dir in components_folder.iterdir():
            if component_dir.is_dir() and not is_allowed_dir(component_dir.name):
                shutil.rmtree(component_dir)

def main():
    # Remove component folders that are not enabled in cookiecutter.json
    remove_disabled_components()

    print("Project initialized, keep up the good work!")  # noqa: F821

if __name__ == "__main__":
    main()
