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
            print(f"Checking {comp} in {dir_name.lower()}")
            print(f"Enabled: {enabled}")
            if enabled and comp in dir_name.lower():
                return True
        return False

    components_folder = Path("src", "components")
    print(f"Current working directory: {Path.cwd()}")
    print(f"Absolute path to components folder: {components_folder.absolute()}")
    print(f"Components folder parts: {list(components_folder.parts)}")
    print(f"Components folder exists: {components_folder.exists()}")

    # Try to list parent directories to see if they exist
    parent = components_folder.parent
    print(f"Parent directory ({parent}) exists: {parent.exists()}")
    grandparent = parent.parent
    print(f"Grandparent directory ({grandparent}) exists: {grandparent.exists()}")

    if components_folder.exists():
        print(f"Components folder exists: {components_folder}")
        for component_dir in components_folder.iterdir():
            print(f"Component dir: {component_dir}")
            print(f"Component dir is dir: {component_dir.is_dir()}")
            if component_dir.is_dir() and not is_allowed_dir(component_dir.name):
                shutil.rmtree(component_dir)
                print(f"Removed component folder: {component_dir}")

def main():
    # Remove component folders that are not enabled in cookiecutter.json
    remove_disabled_components()

    print("Project initialized, keep up the good work!")  # noqa: F821

if __name__ == "__main__":
    main()
