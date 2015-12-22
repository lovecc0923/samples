-module(demo1).

-export([test/0]).

test()->
	[{_,Body},{_,Direction},{_,From},{_,Nickname},{_,SubType},{_,Time},{_,To},{_,Topic},{_,Type}]= jsx:decode(<<"{\"body\":\"我是小灿a1\",\"direction\":0,\"from\":1000,\"nickname\":\"小灿\",\"subType\":2,\"time\":1450752885549,\"to\":1000,\"topic\":\"USER/1000\",\"type\":1}">>),
	Msg1=#{
		    <<"body">> => Body,
		    <<"direction">> => Direction,
			<<"from">> => From,
			<<"nickname">> => Nickname,
			<<"subType">> => SubType,
			<<"time">> => Time,
			<<"to">> => To,
			<<"topic">> => Topic,
			<<"type">> => Type
		   },
	Msg2=#{
		    <<"body">> => Body,
		    <<"direction">> => 1,
			<<"from">> => To,
			<<"nickname">> => Nickname,
			<<"subType">> => SubType,
			<<"time">> => Time,
			<<"to">> => From,
			<<"topic">> => Topic,
			<<"type">> => Type
		   },
Msg2,
	B = list_to_binary("Fuck"),
B,
A= <<"FUCK">>,
binary_to_list(A).