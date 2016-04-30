class Contact < ApplicationRecord
	after_create_commit { ContactBroadcastJob.perform_later self }
end
