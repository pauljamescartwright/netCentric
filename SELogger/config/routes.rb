Rails.application.routes.draw do
	root :to => 'events#index'
	resources :events do
  	resources :operators
	end
	get '/events/:id/public', to: 'events#public'
	get "/events/:event_id/operators/:id/logger", :to => "operators#log"
  # resources :operators
  # resources :events
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  # Serve websocket cable requests in-process
  mount ActionCable.server => '/cable'
end
