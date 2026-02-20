Feature: Wikipedia Language Selector
  As a user
  I want to change Wikipedia's language
  So that I can read content in my preferred language

Background:
  Given I am on Wikipedia homepage

@wikipedia @language-selector
Scenario: Click language selector button
  When I click the language selector button
  Then the language menu should open
  And I should see available languages

@wikipedia @language-switch
Scenario Outline: Switch to different language using selector
  When I click the language selector button
  And I select "<language>" from the language menu
  Then I should be on "<locale>" Wikipedia
  And the page should be in "<language>"
  And content direction should be "<direction>"
  
  Examples:
    | language | locale | direction |
    | English  | en     | ltr       |
    | Español  | es     | ltr       |
    | العربية  | ar     | rtl       |
    | 日本語    | ja     | ltr       |
    | Français | fr     | ltr       |
    | Deutsch  | de     | ltr       |

@wikipedia @language-search
Scenario: Search for specific language
  When I click the language selector button
  Then I should see a language search box
  When I search for "Arabic" in language selector
  Then "العربية" should appear in results
  When I click on "العربية"
  Then I should be on Arabic Wikipedia
  And document direction should be "rtl"