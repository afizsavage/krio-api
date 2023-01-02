Rails.application.routes.draw do
  scope '/api/v1' do
    devise_for :users, defaults: { format: :json }
  end

  scope '/api' do
    namespace :v1, defaults: { format: 'json' } do
      get 'definitions', to: 'definations#index'
    end

    namespace :v1, defaults: { format: 'json' } do
      get 'letters', to: 'letters#index'
    end

    namespace :v1, defaults: { format: 'json' } do
      get 'letters/:id', to: 'letters#show'
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
  end
end
