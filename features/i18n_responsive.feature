@i18n @responsive
Feature: Responsive i18n Testing
  Test translations across different viewport sizes

  Scenario Outline: Responsive layout with translations
    Given locale is "<locale>"
    And I set viewport to <width>x<height>
    When I visit the homepage
    Then text does not overflow containers
    And all translation keys are loaded
    And navigation text should be in <locale>

    Examples:
      | locale  | width | height |
      | en-US   | 1920  | 1080   |
      | de-DE   | 1920  | 1080   |
      | en-US   | 768   | 1024   |
      | de-DE   | 768   | 1024   |
      | en-US   | 375   | 667    |
      | de-DE   | 375   | 667    |
