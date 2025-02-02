@feature_product_browsing
Feature: Product Browsing
  As a page visitor
  I want to browse products by category
  So that I can find items of interest

  Background:
    Given I am on the "Home" page

  @level_e2e @priority_high
  Scenario Outline: Browse Products by Category
    When  I navigate to the "<product_category>" category within Products
    Then  I am on the "<product_category>" product listing page
    And   each product should display its name, detail and image

    Examples:
      | product_category                 |
      | Mission Payloads                 |
      | Power Systems                    |
      | Communication Systems            |
      | Command & Data handling          |
      | Attitude & Orbit Control Systems |
      | Products for Ground Systems      |
      | Structures                       |

  @level_e2e @priority_high
  Scenario: Browse Products by Category
    And   I navigate to the "Mission Payloads" category within Products
    And   I am on the "Mission Payloads" product listing page
    When  I click on the first product's READ MORE button
    Then  I am on the product detail page
