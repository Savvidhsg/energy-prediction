This project explores how Machine Learning (ML) can assist engineers and architects in designing energy-efficient buildings. The focus is on predicting the Heating Load (HL) and Cooling Load (CL) of a building based on design parameters such as wall area, roof area, glazing area, and orientation.

The dataset used is simulated, making it a useful sandbox for experimenting with ML techniques and understanding how different design features influence energy consumption. This is a simplified approach that focuses on key parameters, providing a conceptual demonstration rather than a detailed engineering-grade simulation.

The workflow covers the full process: exploring and analyzing the data, training models, comparing their performance, and building an interactive Streamlit web app for quick predictions. It’s intended as a practical example of applying ML to a real-world-inspired engineering problem.


The dataset was obtained from the UCI Machine Learning Repository. It contains simulated data of various building designs and their respective heating and cooling energy requirements. Each row represents a building design with a combination of architectural features.Features

The dataset includes eight input features:

Relative Compactness: A measure of how compact the building is, influencing heat retention.

Surface Area: Total external surface area of the building.

Wall Area: Total area of the building’s walls.

Roof Area: Total area of the roof.

Overall Height: The height of the building.

Orientation: Cardinal orientation of the building (N, S, E, W).

Glazing Area: Percentage of glazing on the building façade.

Glazing Area Distribution: Distribution of glazing across the building façade.

Targets

Heating Load (HL): Energy required to heat the building.

Cooling Load (CL): Energy required to cool the building.

The first step involved loading the dataset using pandas and performing an initial inspection with .head(), .info(), and .describe(). This allowed verification of the data’s structure, identification of feature ranges, and checking for missing values.

A correlation matrix was then generated to understand how each feature relates to the target variables. The heatmap revealed:

![image](https://github.com/user-attachments/assets/5715b86e-59fc-438a-9fe8-24be71528adc)

Relative Compactness has a strong negative correlation with Heating Load, suggesting more compact designs require less heating energy.

Wall Area and Glazing Area showed positive correlations with energy loads, as larger surface areas increase heat loss or gain.

To better visualize these relationships, scatter plots were created for key features against both Heating Load and Cooling Load.

![image](https://github.com/user-attachments/assets/b98b1ef2-043c-4ecd-b2c0-ca5262193b93)  ![image](https://github.com/user-attachments/assets/e37503e7-84f4-4852-82ef-6b868f192532) ![image](https://github.com/user-attachments/assets/e516d887-3b8d-4ae5-a8e7-2e3cf0ae691c)
![image](https://github.com/user-attachments/assets/08d9461c-4426-4227-bb47-0a14eaf66695) ![image](https://github.com/user-attachments/assets/83b12d0c-b2ff-475d-8cc4-b891f03059a2) ![image](https://github.com/user-attachments/assets/db33a019-ba6c-4f6d-9e27-90f5b92b34bd)

* Relative Compactness: More compact structures lose less heat due to reduced surface area exposure.

* Wall and Roof Areas: Larger areas are prone to higher thermal losses or gains.

* Glazing Area: While windows improve natural lighting, excessive glazing can lead to significant heat loss in winter and overheating in summer.

* Orientation: Determines sun exposure and impacts passive heating/cooling potential.

The findings in this dataset align with real-life architectural principles, reinforcing the idea that thoughtful design choices can dramatically influence a building’s energy efficiency.

After understanding the data and its relationships, the next step was to build predictive models for Heating and Cooling Loads.

The dataset was split into features (X) and target variables (y). Both Heating Load and Cooling Load were treated as separate targets, allowing independent model training for each.

The data was then split into training and testing sets using an 80-20 ratio. Standardization was applied where needed to ensure fair treatment of features, especially for models sensitive to scale.

# Model Selection

Two algorithms were tested to evaluate predictive performance:

* Linear Regression: A simple baseline model to capture linear relationships.

* Random Forest Regressor: An ensemble tree-based method capable of modeling complex, non-linear relationships.

Both models were trained on the training set and evaluated using metrics such as R² score and Mean Squared Error (MSE) on the test set.

# Linear Regression Results

R² Score: 0.91

Mean Squared Error: 9.15

The predictions from Linear Regression showed reasonable performance but missed some of the more intricate relationships between features and energy loads.
![image](https://github.com/user-attachments/assets/56ac2ab4-2a25-4287-ac40-b9997fef75e2)

# Random Forest Results

R² Score: 0.99

Mean Squared Error: 0.24
![image](https://github.com/user-attachments/assets/7d9b9615-1678-4e79-b4bc-a0234a22d6e9)

The difference in model performance highlights the importance of choosing algorithms that align with the underlying complexity of the data. While Linear Regression provides a good first approximation, Random Forest is better suited for datasets with multiple interacting variables and non-linear effects.

These results emphasize that ML can be a powerful tool in guiding design decisions, offering fast predictions even with simplified datasets.

Following the analysis of Heating Load, the same workflow was applied to predict Cooling Load. This involved:

Random Forest Results (Cooling Load)

R² Score: 0.97

Mean Squared Error: 2.93

Random Forest once again demonstrated superior performance, accurately predicting Cooling Load even with complex feature interactions.

![image](https://github.com/user-attachments/assets/497a5384-c4b6-4538-b499-530e6a69d2b1)


In real-world building design, the choice of materials plays a pivotal role in energy efficiency. Materials determine the rate at which heat flows through the building envelope, a property quantified by thermal conductivity (k). This thermal conductivity, combined with thickness and assembly details, contributes to the overall U-value (thermal transmittance) of walls, roofs, and glazing.

* Thermal Conductivity (k): Indicates how well a material conducts heat. Low-k materials like insulation slow heat transfer, while high-k materials like concrete conduct heat more readily.

* U-Value (W/m²K): Represents the rate of heat transfer per unit area and temperature difference. Lower U-values indicate better insulation and lower heat loss.

To bring this physical concept into the model, additional parameters were introduced to represent different material categories for walls, roofs, and glazing. Each category was assigned representative thermal conductivity values to simulate their effect on building energy performance.

This allowed the ML models to account for how upgrading materials (e.g., from standard walls to high-performance insulated walls) changes the predicted Heating and Cooling Loads.

Initially, the impact of changing materials in the simulation was subtle due to the dataset’s scaling. To make these effects more noticeable for demonstration purposes, the thermal conductivity values were adjusted to amplify their influence on energy loads. This change helped users observe clearer differences when experimenting with material types in the Streamlit app, emphasizing how material selection contributes to sustainable design.

To make the project accessible and interactive, a Streamlit web app was developed. This app allows users to select building parameters such as wall area, roof area, glazing area, and material types to instantly predict the expected Heating and Cooling Loads.

Users can experiment with different combinations of features and observe how design choices impact energy requirements. This hands-on interaction provides a more intuitive understanding of the model’s predictions and the role of each parameter.

To provide additional context, the app includes a simple cost estimation module. Users can input the price per kWh for their region, and the app calculates the estimated annual cost of heating and cooling based on the predicted energy loads. While this feature is highly simplified, it offers a practical glimpse into how energy-efficient design decisions can translate into real financial savings over time.


# HOW TO RUN THE APP

Click below to open the app directly in your browser:











