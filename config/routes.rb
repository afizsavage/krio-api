Rails.application.routes.draw do
  resources :letters
  resources :definations
  resources :words
  resources :users
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  # root "articles#index"
end
