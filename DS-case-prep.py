


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
Based on these considerations, my plan is to discuss data preparation, statistical methods, and finally a business stakeholder recommendation. How does this sound?

Methods:
1. Data prep: normalize the data to account for the fact that the sample is noisy, incorporate true number of store visits by taking (the sample foot traffic for store / sample phone population size) * local census population size, incorporate additional data from other highly related retail chains, ensure that for any given socio-demographic dimension that panel phone data matches the underlying census information.
2. Data modeling: compare supervised learning algorithms and use bootstrapping to develop uncertainties on our modeling performance metrics
3. Business reccomendation: write up a design doc and slide deck that facilitates stakeholder’s ability to make actionable insights from our solution. Emphasize the uncertainty in our revenue prediction, since shorting a stock is high-risk.

Conclusion:
With a supervised model that correlates foot traffic data to quarterly revenue, stakeholders can make data-informed decisions on whether to buy or short the given retail chain’s stock. However, it’s key to not make these decisions entirely data-driven, as the modeling outputs should be considered alongside other financial information and the model uncertainty should be taken into account to have a better understanding of the risks in trusting the predictions.
""",

"""
Google, Airline Ticket Price Forecasting: How would you forecast airline ticket prices and how would you correct the Covid impact on the forecast?
""":
"""
Clarify:
1. Do I need to forecast the ticket prices on a short-term horizon or long-term horizon? (A: six months ahead)
2. What kind of dataset do I have to build the forecasting model? (A: Let’s say you have three years of historical price data and any macroeconomic signals of your choice.)

Constrain:
I suppose Google’s flight search product has an airline prediction feature enabling users to plan travel around predicted ticket costs. This feature provides a lot of value to users.

Plan:
Based on these considerations, my plan is to discuss data preparation, statistical methods, and finally a stakeholder recommendation. How does this sound?

Methods:
1. Data prep: To start, I would conduct an EDA to confirm registration between the features and labels and confirm the data validity. I would check for outliers, missing values, seasonality, and trends.
2. Modeling: Given that the problem is long-term forecasting, I would either need to take a window-based approach using a classical TS algorithm (take output and re-run for next window of time) or use a supervised model which enables extrapolation. For the latter, we could incorporate time-series and seasonality features. We could consider a design that uses separate models for differing airlines and locations or we could consider a design that incorporates these as features. I would use Mean Absolute Percentage Error for measuring model performance because this metric is easy to explain to stakeholders. For macro-economic features we could use unemployment rate, GDP growth, and population density. These would be helpful because demand fluctuates with economic conditions (bad economy, people spend less, demand drops, price drops). I would leverage additional features around COVID impact such as lockdown indicators and confirmed covid case rates.

Conclude:
The google flights product relies on forecasting flight costs to inform users about when they should travel. Time series models can be used with a number of travel, macroeconomic, and COVID features to provide this product.
""",

"""
Amazon, Propensity Modeling for AWS Sales: How would you identify key attributes that predict whether a customer will repeat a purchase on AWS products?
""":
"""
Clarify:
1. I know that the AWS service provides various business solutions from computing, database, and AI tools. Do I need to predict which product a particular customer will likely convert to again? Or, should I focus on whether a customer will convert again at all?
2. Thank you for the clarification. I have another question: what do you mean by a “repeat purchase?” I assume that the AWS sales team provides enterprise solutions. In this case, they most likely care about long-term usages such as annual subscriptions or contracts. Would the repeat purchase be based on if they purchased a product then another one immediately? Or, would it be based on a long-term horizon, meaning that a customer purchased a product this year and again the following year. (In this case, a repeat purchase occurs when a customer purchased a product the first year and purchased again the following year.)

Constrain:
I can tell that this problem involves propensity modeling given that the problem involves finding attributes that predict customer conversion.

Plan:
Based on these considerations, my plan is to discuss data preparation, statistical methods, and finally a stakeholder recommendation. How does this sound?

Methods:
1. Data Prep: I can think of three types of data: (1) user profile (2) user-product behavior, and (3) marketing engagements. Each data type contains the following attributes: User profile - business name, industry, years in operation, and location. User-product behavior - the type of product purchased and engagement metrics (i.e. average # of active sessions the past 1 month), and new products browsed on the AWS platform. Marketing engagements - newsletter sign-ups, free-trial enrollments and advertisement clicks.
2. EDA/Descriptive Stats: I would conduct an exploratory data analysis to understand how the attributes correlate with the target variable - the recurrent purchase of a product the following year. In addition, the EDA informs how I should clean and preprocess the data for modeling.
3. Modeling: Label derived from purchase indicator, binary on whether a user purchased again in the following year. I would need at least two years of data. We could use log regression or random forest regression. F1 score to balance precision and recall.
4. Post-modeling: How would you address the main question on identifying attributes that lead to a repeat purchase? Use features with statistical significance and rank based on coefficient values. Can use a partial dependence plot to understand the probablity of conversion across a variable range while holding others constant, which enables us to isolate a subset of values in a categorical variable or a bracket within a continuous variable that is highly correlated with the repeat conversion.

Conclude:
There are two ways this could be helpful for the sales team. First, the propensity model helps detect users that are most likely to convert again. The sales team can invest their efforts in high-intent customers as there are less time and $ cost involved in converting those users compared to the low-intent customers. Secondly, once the high-intent users are identified, I can create customer segments based on key attributes. The segments are helpful for the sales team in creating custom sales funnel for each segment.

""",

"""
Amazon, Fraud on Amazon with No Labels: Presume that you have a dataset with 30 days of IP address, device ID, and email address. How would you classify an Amazon user as a fraudster or not given that you do not have labels?
""":
"""
Question:
1. Can I start by asking if the fraudsters that need to be detected are among the sellers or consumers? It’s my experience that behaviors are quite different whether the fraudster is on the seller-side or consumer-side. (Consumers)
2. Great. I have a follow-up question. There could be multiple types of fraudulent activities on the consumer side. Can I assume that they are fraudsters who commit chargebacks? An example could be fraudsters who purchased and received goods then claim that they did not make the transaction to receive a refund? (Yes)
3. I have another follow-up question, which is about the data itself. Is it fair to assume that a user could have multiple IP addresses, device ID’s and email addresses?

Constrain:
I think I can start ideating a potential solution. It’s my understanding that a fraudster would create multiple accounts using a combination of different IP addresses, device ID’s and email addresses.
A normal user would most likely have one email address tied to a single IP address which is usually his home internet. However, a fraudster could have multiple email addresses linked to an IP address because he is attempting to establish multiple accounts.
Having multiple accounts would allow him to continue committing chargeback fraud even if one of the accounts gets banned.

Methods:
1. Data Prep/Feature Engineering: Well, we need to derive a feature set that counts the distinct IP addresses per email address for the past 30 days. We can use this strategy for other combinations of ID variables. Here’s a sample of features that can be created:
# of distinct email addresses per IP address the past 7 days
# of distinct email addresses per IP address the past 14 days
# of distinct email addresses per IP address the past 30 days
# of distinct device IDs per email address the past 7 days

2. Statistical methods: Option 1: rule-based approach where we look at the probability distribution per feature. Apply a threshold on the 99th percentile. We apply the threshold across the variables to derive a subset of users who are the most suspicious. Obviously, this is not model-based, but it should provide a good start to labeling potential fraudsters. Now, we need to verify those labels so we send the subset to the review team for verification on the label. This will help us identify the precision of the system. Option 2: The other idea uses a deep learning model. An auto-encoder is an unsupervised algorithm that helps flag outliers which is what we want to do on the feature set. We can use the reconstruction error (measured in MSE) to identify users which high outlier scores. We can repeat the procedure of manually verifying those users by sending those to the review team.

3. Stakeholder reccomendation/Conclude: Last step is to verify the labels with the review team.
"""
}

from numpy.random import randint
i = randint(0, len(case_questions))
entry_list = list(case_questions.items())
print(entry_list[i][0])
bool = input("Want the answer (reply 'Yes'/'No'):?")

if (bool != 'No') and (bool != 'None'):
    print(entry_list[i][1])
