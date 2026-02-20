@i18n
Feature: Multi-language Login
  As a user
  I want to see the login page in my language
  So that I can understand the interface

  Scenario Outline: Login page in different languages
    Given locale is "<locale>"
    And I am on the login page
    Then the login title should be "<title>"
    And I should see "<username_label>"
    And I should see "<password_label>"

    Examples:
      | locale  | title            | username_label        | password_label  |
      | en-US   | Login            | Username              | Password        |
      | es-ES   | Iniciar Sesión   | Nombre de Usuario     | Contraseña      |
      | fr-FR   | Connexion        | Nom d'utilisateur     | Mot de passe    |
      | de-DE   | Anmelden         | Benutzername          | Passwort        |

  Scenario Outline: RTL language support
    Given locale is "<locale>"
    And I am on the login page
    Then the page direction should be RTL
    And text direction should be "rtl"

    Examples:
      | locale  |
      | ar-SA   |
