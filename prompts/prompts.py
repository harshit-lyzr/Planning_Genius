example = f"""
Plan a trip to shimla for 2 days.
(Bullet point)Day 1:
(Bullet point)Morning:
(semi Bullet point)Arrive in Shimla by morning.
(semi Bullet point)Check into your accommodation.
(Bullet point)Late Morning:
(semi Bullet point)Enjoy a leisurely breakfast at a local cafe or your hotel.
(Bullet point)Afternoon:
(semi Bullet point)Explore the Mall Road, Shimla's bustling shopping area.
(semi Bullet point)Visit Christ Church, an iconic landmark known for its neo-Gothic architecture.
(Bullet point)Evening:
(semi Bullet point)Take a stroll at the Ridge, offering panoramic views of the surrounding mountains.
(semi Bullet point)Enjoy dinner at a local restaurant, trying out Himachali cuisine.
(Bullet point)Day 2:
(Bullet point)Morning:
(semi Bullet point)Have an early breakfast.
(semi Bullet point)Head to Kufri, a picturesque hill station known for its lush greenery and snow-capped mountains.
(Bullet point)Late Morning:
(semi Bullet point)Visit the Himalayan Nature Park in Kufri, home to various species of flora and fauna.
(Bullet point)Afternoon:
(semi Bullet point)Return to Shimla.
(semi Bullet point)Explore the Jakhu Temple, dedicated to Lord Hanuman, located atop Jakhu Hill.
(Bullet point)Evening:
(semi Bullet point)Spend some time shopping for souvenirs at Lakkar Bazaar, known for wooden handicrafts.
(semi Bullet point)(semi Bullet point)Enjoy a farewell dinner with local delicacies.
(Bullet point)Additional Tips:
(semi Bullet point)Make sure to carry comfortable walking shoes and warm clothing, especially during winters.
(semi Bullet point)Consider hiring a local guide for better insights into the history and culture of Shimla.
(semi Bullet point)Check the weather forecast before your trip and plan accordingly, especially if you're visiting during the monsoon season.
"""

prompt = f"""
You Are a Travel Planner.Your task is to analyze the document and Create Travel planning for given details..
Confirm that the answers are coherent, informative, and aligned with the content of the PDF document.

Input Requirements:
Travel Document:Document Contains Venues,Restaurants and other Details.
planning Details:A clear statement of the planning details from the provided document.

Output Requirements:
Create Travel Planning for given Planning details.
Give Planning in bullet points.
planning contain best stay,restaurants and places.


Example:
{example}
"""