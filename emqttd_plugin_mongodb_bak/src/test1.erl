-module(test1).

-export([check/3,query/1,hash/2]).

check(Username,Password,HashType) ->
  case query(Username) of
    {ok, [Record]} ->
		{ok,PassHash} = maps:find(<<"password">>, Record),
	  	check_pass(PassHash,Password,HashType);
    {ok, []} ->
	  {error, notfound}
  end.

query(Username) ->
  application:start(bson),
  application:start(crypto),
  application:start(mongodb),
  Database = <<"db0">>,
  Collection = <<"mqtt_user">>,
  {ok, Connection} = mongo:connect([{database, Database}]),
  Cursor = mongo:find(Connection, Collection, {<<"username">>, Username}),
  Result = mc_cursor:rest(Cursor),
  mc_cursor:close(Cursor),
  {ok, Result}.

check_pass(PassHash, Password, HashType) ->
  case PassHash =:= hash(HashType, Password) of
    true -> ok;
    false -> {error, password_error}
  end.

hash(sha256, Password)  ->
    hexstring(crypto:hash(sha256, Password)).

hexstring(<<X:256/big-unsigned-integer>>) ->
    iolist_to_binary(io_lib:format("~64.16.0b", [X])).