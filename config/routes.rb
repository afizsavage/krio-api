Rails.application.routes.draw do
  namespace :v1, defaults: { format: 'json' } do
    get 'letters', to: 'letters#index'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'users', to: 'users#index'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'words', to: 'words#index'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'letters/:id', to: 'letters#show'
  end

  namespace :v1, defaults: { format: 'json' } do
    get 'definitions', to: 'definations#index'
  end
end
