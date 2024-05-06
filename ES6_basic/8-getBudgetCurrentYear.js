function getCurrentYear() {
    const date = new Date();
    return date.getFullYear();
  }
  
  export default function getBudgetForCurrentYear(income, gdp, capita) {
    const year = getCurrentYear(); // Call once and store in a variable to avoid multiple calls
    const budget = {
      [`income-${year}`]: income,
      [`gdp-${year}`]: gdp,
      [`capita-${year}`]: capita
    };
  
    return budget;
  }
  