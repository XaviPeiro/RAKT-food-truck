# RAKT-food-truck

# 🧠 Considerations
- I will assume "permit" is the data that identifies the "food-truck". However:
  - In the dataset there are **different locations for the same food-truck** and **"dayshours" are NaN**, therefore:
    - I am **cleaning the dataset** and leaving **only one location per food-truck (i.e.: permit)**.
    - I am assuming it will be a scheduled service to update food-trucks' location.
  - Could be interesting to create a specific model field it (permit, i.e.: the id).
- Could be interesting to create a specific model field for **FoodTruck.address**.
- I am not modelling food type, instead I will use "food description" for the sake of simplicity.
- So far not taking care about when a permit expires.
- No tests, sadly.
- No Swagger. 😑
- No venvs 😓
---
- I have invested ~3.75h in this project.

# 👾 Requirements
- Docker
- Docker Compose
- jq (optional)

# 🚀 Usage
- Init the project.
```zsh
docker-compose up -d
```

## Website
- Just open in your browser:
  - **GET ALL TRUCKS**: localhost:8000/food-truck/
  - **GET NEAREST TRUCKS**: localhost:8000/food-truck/get-nearest?latitude=37.76008693198698&longitude=-122.41880648110114

## Command Line
- Get **ALL** Food Trucks available (**not nearest, ALL**)
```zsh
docker-compose exec app sh -c "curl -XGET localhost:8000/food-truck/ | jq"
```
- Get **NEAREST** Food Trucks available
```zsh
docker-compose exec app sh -c "curl -XGET 'localhost:8000/food-truck/get-nearest/?latitude=37.76008693198698&longitude=-122.41880648110114' | jq"
```


###