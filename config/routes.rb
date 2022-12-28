Rails.application.routes.draw do
  namespace :v1, defaults: { format: 'json' } do
    get 'definitions', to: 'definations#index'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'letters', to: 'letters#index'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'letters/:id', to: 'letters#show'
  end

  # namespace :v1, defaults: { format: 'json' } do
  # get 'users', to: 'users#index'
  # devise_for :users
  # end

  namespace :v1, defaults: { format: 'json' } do
    #   post 'users', to: 'users#create'
    devise_for :users
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'words', to: 'words#index'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'words/:id', to: 'words#show'
  end

  namespace :v1, defaults: { format: 'json' } do
    post 'words', to: 'words#create'
  end
  # namespace :v1, defaults: { format: 'json' } do
  #   post 'words/search/:q', to: 'words#search_by_title'
  # end
end
