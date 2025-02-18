<!-- Cookiecutter Template Transformation Plan -->

# Cookiecutter Template Transformation Plan

## Phase 1: Define and Configure Template Variables

- Create a cookiecutter configuration file (typically cookiecutter.json at the repository root) that declares all our dynamic fields:
  - Pages (YAML/JSON for pages with layout definitions)
  - Application Navigation config (YAML/JSON for navigation items linking to pages)
  - User management (boolean, default false)
  - Theme mode ("dark" or "light", default "dark")
  - Components (list, e.g., tables)
  - Landing Page (boolean, default false)
- Variable names should be in lowercase with underscores separating words.

## Phase 2: Templatize the Repository Structure

- Review the current repository layout to identify files, directories, and content that should change based on input variables.
- Replace static text and filenames with Jinja2 placeholders (e.g., using {{ cookiecutter.variable_name }}).
- Name folders or files dynamically if needed, so that aspects like page names or component directories can be generated from the configuration.

## Phase 3: Dynamic Content Generation & Conditional Inclusions

- For "Pages" and "Application Navigation config":
  - Implement templates or scaffolding scripts that generate page files and navigation metadata based on the provided YAML/JSON config.
- For "User management":
  - Use Jinja2 conditionals to include extra screens (signin, signup, etc.) only when enabled.
- For "Theme mode":
  - Insert conditional logic or parameter integration in style files/assets to switch between dark/light themes.
- For "Components":
  - Templatize inclusion of specific components (e.g., include extra code/templates if "tables" is mentioned).
- For "Landing Page":
  - Conditionally include a landing page module or modify routing if enabled.

## Phase 4: Testing the Cookiecutter Template

- Run the cookiecutter command locally on the modified repository to generate a project instance.
- Validate that all input configuration values are correctly rendered into the scaffolded project (e.g., pages, navigation, user management screens, theme, etc.).
- Iterate on the template logic (Jinja2 syntax, conditional blocks) until the generated output meets expectations.

## Phase 5: Documentation and Final Cleanup

- Update the README (or add separate documentation) to explain how to use the template with cookiecutter, including links to the official cookiecutter tutorials.
- Document each configurable field and how its value impacts the generated project.
- Ensure code comments, instructions, and any edge cases are clearly addressed.
- Perform a final cleanup (removing any debug scaffolding or extra files) so the repository is production-ready as a cookiecutter template.

<!-- End Cookiecutter Template Transformation Plan -->
