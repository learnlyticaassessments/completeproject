Feature: Wikipedia Multi-language Support

Scenario Outline: Navigation in different languages
  Given I visit Wikipedia in "<locale>"
  Then I should see main page title in "<language>"
  And date format should match "<locale>"
  And search placeholder should be in "<language>"
  
  Examples:
    | locale | language | 
    | en     | English  |
    | es     | Spanish  |
    | ar     | Arabic   |
    | ja     | Japanese |



