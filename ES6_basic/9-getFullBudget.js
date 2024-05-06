import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) {  // ES6 method shorthand
      return `$${income}`;
    },
    getIncomeInEuros(income) {    // ES6 method shorthand
      return `${income} euros`;
    },
  };

  return fullBudget;
}
