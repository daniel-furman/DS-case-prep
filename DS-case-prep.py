


case_questions = {

"""
Citadel, Retailer Revenue Estimation: Say you wanted to estimate the physical store sales for a publicly traded retail chain in the US. You have access to third-party foot traffic data for each store that was derived from anonymized GPS data collected from a panel of 10 million phones. At a high-level, how could you use this food traffic dataset to predict the chain’s in-store revenue?
""" :
"""
Clarify:
1. What’s the use-case for predicting in store revenue? I’m guessing it’s for making investment decisions.
2. We are trying to make revenue estimates for the entire chain - not for each store, correct?
3. What’s the granularity needed for our revenue prediction? I’m assuming it's quarterly due to quarterly earnings for public stocks.
4. Is the third-party foot traffic data source trusted? Do they have a history of producing accurate data?
5. Can you tell me more about this data source - what do the rows and columns look like? I presume each row is for a given store, and the columns will include some kind of non-normalized foot traffic value based on devices tracked for a given time period. I’m guessing it's at a daily granularity?

Constrain:
The key relationship we are aiming to capture in our forecasting model is how foot traffic data corresponds to in-store revenue, a prediction that would enable investors to make more informed decisions pre revenue release. At a high-level, the approach would be to run a predictive model based on an aggregated quarterly measure of foot traffic across the physical stores.

Plan:
Based on this thesis, my plan is to discuss data preparation, statistical methods, and finally a business stakeholder recommendation. How does this sound?

Methods:
1. Data prep: normalize the data to account for the fact that the sample is noisy, incorporate true number of store visits by taking (the sample foot traffic for store / sample phone population size) * local census population size, incorporate additional data from other highly related retail chains, ensure that for any given socio-demographic dimension that panel phone data matches the underlying census information.
2. Data modeling: compare supervised learning algorithms and use bootstrapping to develop uncertainties on our modeling performance metrics
3. Business reccomendation: write up a design doc and slide deck that facilitates stakeholder’s ability to make actionable insights from our solution. Emphasize the uncertainty in our revenue prediction, since shorting a stock is high-risk.

Conclusion:
With a supervised model that correlates foot traffic data to quarterly revenue, stakeholders can make data-informed decisions on whether to buy or short the given retail chain’s stock. However, it’s key to not make these decisions entirely data-driven, as the modeling outputs should be considered alongside other financial information and the model uncertainty should be taken into account to have a better understanding of the risks in trusting the predictions."""

}

from numpy.random import randint
i = randint(0, len(case_questions))
entry_list = list(case_questions.items())
print(entry_list[i][0])
bool = input("Want the answer (reply 'Yes'/'No'):?")

if (bool != 'No') and (bool != 'None'):
    print(entry_list[i][1])
