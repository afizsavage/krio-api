class Word < ApplicationRecord
    belongs_to :user
    belongs_to :letter
    has_one :defination
end
