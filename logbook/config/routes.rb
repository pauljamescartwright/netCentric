Rails.application.routes.draw do
  get 'contact/index'

  get 'contact/show'

  get 'contact/new'

  get 'contact/create'

  get 'contact/edit'

  get 'contact/update'

  get 'contact/destroy'

  get 'operator/index'

  get 'operator/show'

  get 'operator/new'

  get 'operator/create'

  get 'operator/edit'

  get 'operator/update'

  get 'operator/destroy'

  root :to => 'special_event#index'

  get 'special_event/show'

  get 'special_event/new'

  get 'special_event/create'

  get 'special_event/edit'

  get 'special_event/update'

  get 'special_event/destroy'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html

  # Serve websocket cable requests in-process
  # mount ActionCable.server => '/cable'
end
