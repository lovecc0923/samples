-module(test).

-export([init/0,id/1,type/1,timestamp/0,init1/0]).

init() ->
  application:start(bson),
  application:start(crypto),
  application:start(mongodb),

  Host = "114.119.6.150",
  Port = 27017,
  Database = <<"db0">>,
  Collection = <<"TopicHistory">>,
  
  UserId = 10087,
  Nickname = unicode:characters_to_binary("艹他么乱码"),
  Body = unicode:characters_to_binary("艹他么乱码......"),
  Map1 = #{
    <<"type">> => 1,				
    <<"userId">> => 10086,		
    <<"id">> => <<"USER/10020">>,	
    <<"name">> => Nickname,		
    <<"desc">> => Body,			
    <<"time">> => 11860056656,	
    <<"count">> => 198			
  },
  Id = <<"USER/10086">>,
  
  {ok, DBConnection} = mongo:connect([{database, Database}, {host, Host}, {port, Port}]),
  case mongo:count(DBConnection, Collection, {<<"_id">>, UserId}) of
    0 ->
      mongo:insert(DBConnection, Collection, #{<<"_id">> => UserId, <<"topics">> => [Map1]});
    _ ->
	  case mongo:count(DBConnection, Collection, {<<"_id">>, UserId, <<"topics.id">>, Id}) of
		  0 -> 
			Q = #{<<"_id">> => UserId},
	  		Ops = #{<<"$addToSet">> => #{<<"topics">> =>  #{<<"$each">> => [Map1]}}},
	  		mongo:update(DBConnection, Collection, Q, Ops);
		  _ -> "exists,skip"
      end
  end,
  mongo:disconnect(DBConnection).

init1()->
	A= <<"fuck">>,
	binary_to_list(A).
%%   Host = "114.119.6.150",
%%   Port = 27017,
%%   Database = <<"db0">>,
%%   Collection = <<"TopicHistory">>,
%%   UserId = 10087,
%%   Id = "USER/10089",
%%   
%%   {ok, Connection} = mongo:connect([{database, Database}, {host, Host}, {port, Port}]),
%%   Count1 = mongo:count(Connection, Collection, {<<"_id">>, UserId}, 0),
%%   Count1,
%%   mongo:disconnect(Connection).
	
id(Topic) ->
	Index = string:chr(Topic, 47),
	string:substr(Topic, Index + 1).

type(Topic) ->
	Index = string:chr(Topic, 47),
	case string:substr(Topic, 1, Index - 1) of
		"USER" -> 1;
		"GROUP" -> 2;
		"SYSTEM" -> 3;
		_ -> 0
	end.

timestamp() -> 
  {M, S, _} = os:timestamp(),
  M * 1000000 + S.

