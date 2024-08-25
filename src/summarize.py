from transformers import pipeline, BartTokenizer

def get_summary(full_text):
    # model_name = "facebook/bart-large-cnn"
    model_name = "facebook/bart-base"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    tokenizer.clean_up_tokenization_spaces = True
    summarizer = pipeline("summarization", model=model_name, device=-1, tokenizer=tokenizer)
    summary = summarizer(full_text, max_length=200, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    ip = """ New York (CNN)When Liana Barrientos was 23 years old, she got married in Westchester County, New York.
A year later, she got married again in Westchester County, but to a different man and without divorcing her first husband.
Only 18 days after that marriage, she got hitched yet again. Then, Barrientos declared "I do" five more times, sometimes only within two weeks of each other.
In 2010, she married once more, this time in the Bronx. In an application for a marriage license, she stated it was her "first and only" marriage.
Barrientos, now 39, is facing two criminal counts of "offering a false instrument for filing in the first degree," referring to her false statements on the
2010 marriage license application, according to court documents.
Prosecutors said the marriages were part of an immigration scam.
On Friday, she pleaded not guilty at State Supreme Court in the Bronx, according to her attorney, Christopher Wright, who declined to comment further.
After leaving court, Barrientos was arrested and charged with theft of service and criminal trespass for allegedly sneaking into the New York subway through an emergency exit, said Detective
Annette Markowski, a police spokeswoman. In total, Barrientos has been married 10 times, with nine of her marriages occurring between 1999 and 2002.
All occurred either in Westchester County, Long Island, New Jersey or the Bronx. She is believed to still be married to four men, and at one time, she was married to eight men at once, prosecutors say.
Prosecutors said the immigration scam involved some of her husbands, who filed for permanent residence status shortly after the marriages.
Any divorces happened only after such filings were approved. It was unclear whether any of the men will be prosecuted.
The case was referred to the Bronx District Attorney\'s Office by Immigration and Customs Enforcement and the Department of Homeland Security\'s
Investigation Division. Seven of the men are from so-called "red-flagged" countries, including Egypt, Turkey, Georgia, Pakistan and Mali.
Her eighth husband, Rashid Rajput, was deported in 2006 to his native Pakistan after an investigation by the Joint Terrorism Task Force.
If convicted, Barrientos faces up to four years in prison.  Her next court appearance is scheduled for May 18.
"""
    ip2 = """"
    Motor Health Other Motor Health Other File a Claim File Health Claim File Motor Claim for Garages Check Health Claim Status Digit Cashless Garages Digit Cashless Hospitals Anywhere Cashless Hospitals Renewals Become an Agent Check Pending Challans FREE Credit Score Check Download Digit Policy Download Digit App Digit Play Marine Open Certificate Issuance Grievance Redressal Procedure IRDAI's Call Centre Feedback Survey Our WhatsApp number is a chat only number. One stop solution for all your queries! Our WhatsApp number is a chat only number. One stop solution for all your queries! More Products Motor Health Other Support Our WhatsApp number is a chat only number. One stop solution for all your queries! Mobile Insurance Download the App Now and Join the Waitlist Download the Digit App India’s smartphone market is dynamic, and people are spoilt for choice as too many smartphone brands are available.A few affordable brands like Xiaomi and mid-range smartphone brands, including Vivo, Oppo, Realme, etc., have consistently risen to the top. Premium mobile brands like Apple and Samsung have also managed to maintain their market share in India.In Quarter 3 of 2023, the smartphone industry in India registered 43 million shipments and a 3% y-o-y fall in smartphone sales, as per recent reports. However, 5G smartphone shipments have risen to a market share of 50%.So, if you wish to know the top smartphone brands in India, refer to the table below that shows the market share of each of the top 7 smartphone brands in India India’s smartphone market is dynamic, and people are Explore the top mobile brands in India 2024, featuring Vivo, Samsung, Apple, and more. Get insights on market share and standout features Photo of the day: In arms Mpox epidemic disinformation debunked Top 8 of the world's biggest diamond finds From tracking the pre- and post-independence journey of storied Indian brands to a new World Pickleball League, our top stories of the week A holistic safari to Sasan Gir Photo of the day: On winning streak Gamescom: Microsoft seeks to win over new players 'Modern Family,' 'Friends,' 'Sex and the City' - could the characters have actually afforded their homes? Air India: The story of a lost opportunity Can senior politicians teach executives how to lead? Photo of the day: Protests return to streets New 'Call of Duty' and 'Borderlands 4' games announced at Gamescom Liverpool house used for early Beatles gigs becomes holiday rental How the 146-year-old Crompton has managed to stay afloat Lessons and reforms for a fragile financial system Discover the top-rated mobile phones in India, carefully curated for performance, features, and value. Find your perfect smartphone from our expertly compiled list of the best options available in the market.
    """
    print(get_summary(ip))
