class Operator < ApplicationRecord
	belongs_to :special_event_station
	has_many :contacts
end
