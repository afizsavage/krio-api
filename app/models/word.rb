class Word < ApplicationRecord
  belongs_to :user
  belongs_to :letter
  has_one :defination

  accepts_nested_attributes_for :defination
end
