class User < ApplicationRecord
  has_many :words
  has_many :definations
end
