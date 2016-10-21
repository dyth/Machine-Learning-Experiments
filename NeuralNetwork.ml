(* Useful function *)
fun ArrtoList arr = Array.foldr (op ::) [] arr;

(* ========================== Neural Network Data =========================== *)
(* no. of stages [no. of neurons] *)
val initialise = Array.fromList [1, 4, 2];
(* return number of levels in neuron *)
val lev = Array.length(initialise) - 1;
(* return number of neurons in nth level *)
fun getno n = Array.sub (initialise, n);

(* no. of input values *)
val input = 100;

(* return nth inputs value *)
fun getin n = Array.sub(inputs, n);
(* no. of training examples *)
val training = 100;

(* expected output values *)
val expected = [0.0, 1.0];

(* Learning rate *)
val eta = 0.6;
(* Number of training examples *)
val m = ref 1.0;


(* ======================== Random Number Generation ======================== *)
local val a = 16807.0 and m = 2147483647.0 and randnum = ref 1.0
in fun random () =
     let val t = a * (!randnum)
     in randnum := t - m * real(floor(t/m));
	t/m - real (floor(t/m))
     end
end;



(* DUMMY input values *)
val inputs = Array.tabulate (input, fn x => random());


(* Gaussian Distribution *)
fun gauss () = Math.pow(Math.e,
		~ (Math.pow(real(input) * random(), 2.0) / (2.0 * real(input))))
				/ Math.sqrt(2.0 * Math.pi * real(input));


(* ==================== Operations on values in network ===================== *)
(* return number of neurons in n-1 stage *)
fun prev 0 = input
  | prev n = Array.sub (initialise, n-1);

(* Create network, variables are all random numbers *)
val network =
    (* w = no. of weights, output initialised to 0.0 *)
    let	fun create w = (Array.tabulate(w, fn a => random()), ref (random()), ref 0.0);
    in Array.tabulate (Array.length(initialise),
			      fn a => Array.tabulate (Array.sub (initialise, a),
						      fn b => create (prev a)))
    end;


(* ========================== Get values in network ========================= *)
(* Return output of neuron j at level l *)
fun get j l    = !(#3 (Array.sub (Array.sub (network, l), j)));
(* Return array of weights of neuron j at level l *)
fun getws j l  = #1 (Array.sub (Array.sub (network, l), j));
(* Return nth weight of neuron j at level l*)
fun getw n j l = Array.sub (#1 (Array.sub (Array.sub (network, l), j)), n);
(* Return bias of neuron j at level l*)
fun getb j l   = !(#2 (Array.sub (Array.sub (network, l), j)));


(* ========================= Set values in network ========================== *)
(* Update nth weight of neuron j at level l to w *)
fun updatew n j l w = Array.update (#1 (Array.sub (Array.sub (network, l), j)), n, w);
(* Update bias of neuron j at level l to b *)
fun updateb j l b = (#2 (Array.sub (Array.sub (network, l), j))) := b;
(* Update value of neuron j at level l to n *)
fun set j l n = (#3 (Array.sub (Array.sub (network, l), j))) := n;


(* ============================== Forward Pass ============================== *)
(* Computes weights and bias for neuron j in level l *)
local fun dotprod _ _  []        = 0.0
	| dotprod j ~1 (w :: ws) = (getin j) * w + dotprod (j + 1) ~1 ws
	| dotprod j l  (w :: ws) = (get j l) * w + dotprod (j + 1) l  ws
in fun getexp j l = (getb j l) + dotprod 0 (l-1) (ArrtoList (getws j l))
end;
(* Sigmoidal function *)
fun sigmoid z = 1.0 / (1.0 + Math.pow((Math.e), z));
(* Computes value for neuron j in level l *)
fun neuron j l = set j l (sigmoid (getexp j l));

(* A complete forward pass for the whole network *)
fun forward () = app (fn y => app (fn z => neuron z y)
				  (List.tabulate(getno y, fn a => a)))
		                  (List.tabulate(lev + 1, fn x => x));
(* Returns list of the output neuron values *)
fun output () = List.tabulate(Array.sub(initialise, lev), (fn j => get j lev));


(* ============================= Backpropagation ============================ *)
(* Quadratic cost function *)
fun qcost () =
  let fun difference []        []        = 0.0
	| difference (x :: xs) (y :: ys) = Math.pow((x-y),2.0) +difference xs ys
  in (difference expected (output())) / real (2 * training)
  end;

(* TODO: Cross-entropy cost function
fun ccost () = *)

(* Create network: [weight errors], bias error, error *)
val backnetwork =
    (* w = no. of weights, output initialised to 0.0 *)
    let	fun create w = (Array.tabulate(w, fn a => 0.0), ref 0.0, ref 0.0);
    in Array.tabulate (Array.length(initialise),
			      fn a => Array.tabulate (Array.sub (initialise, a),
						      fn b => create (prev a)))
    end;

(* Get error in neuron j level l *)
fun geterr j l    = !(#3 (Array.sub (Array.sub (backnetwork, l), j)));
(* Return array of weight errors of neuron j at level l *)
fun getwerrs j l  = #1 (Array.sub (Array.sub (network, l), j));
(* Get nth weight error in neuron j at level l *)
fun getwerr n j l = Array.sub (#1 (Array.sub (Array.sub (backnetwork,l),j)), n);
(* Get bias error of neuron j at level l *)
fun getberr j l   = !(#2 (Array.sub (Array.sub (backnetwork, l), j)));

(* Update nth weight error of neuron j at level l to w *)
fun upwerr n j l w = Array.update (#1 (Array.sub (Array.sub (backnetwork, l), j)), n, w);
(* Update bias error of neuron j at level l to b *)
fun upberr j l b   = (#2 (Array.sub (Array.sub (backnetwork, l), j))) := b;
(* Update error of neuron j at level l to n *)
fun seterr j l n   = (#3 (Array.sub (Array.sub (backnetwork, l), j))) := n;

local (* Error in neurone j, layer l *)
    fun bdotprod _ 0 _ = 0.0
      | bdotprod j n l = (getw j n l) * (geterr n l) + bdotprod j (n-1) l;
    (* First differential of sigmoidal function *)
    fun sigdif x = Math.pow(Math.e,x) / Math.pow(1.0 + Math.pow(Math.e,x), 2.0);
in fun error j l = if (l = lev)
    then seterr j l (((get j l) - List.nth(expected, j)) * sigdif (getexp j l))
    else seterr j l ((bdotprod j ((getno(l+1))-1) (l+1)) * sigdif(getexp j l))
end;
(* Set bias error change of neuron j level l *)
fun berr j l = upberr j l (geterr j l);
(* Set nth weight error change of neuron j level l *)
fun werr n j l = upwerr n j l ((get j l)*(geterr j l));

(* A complete backward pass for errors *)
fun backpass () = app (fn y => app (fn z => error z y)
				  (List.tabulate(getno y, fn a => a)))
		                  (List.tabulate(lev + 1, fn x => lev-x));
(* Update all biases *)
fun backbias () = app (fn y => app (fn z => berr z y)
				  (List.tabulate(getno y, fn a => a)))
		                  (List.tabulate(lev + 1, fn x => x));
(* Update all weights *)
fun backweight () = app (fn y => app (fn z => (app (fn c => werr c z y) (List.tabulate(prev y, fn b => b)))) (List.tabulate(getno y, fn a => a)))
		        (List.tabulate(lev + 1, fn x => x));
(* Complete backward pass, update all biases and weights *)
fun back () = (backpass (); backbias(); backweight());

(* ======================== Updates weights and bias ======================== *)
fun updateweight n j l = updatew n j l (eta*(getwerr n j l)/(!m));
fun updatebias j l = updateb j l (eta*(getberr j l)/(!m));

fun allweights () = app (fn y => app (fn z => (app (fn c => updateweight c z y) (List.tabulate(prev y, fn b => b)))) (List.tabulate(getno y, fn a => a)))
		        (List.tabulate(lev + 1, fn x => x));
fun allbias () = app (fn y => app (fn z => updatebias z y)
				  (List.tabulate(getno y, fn a => a)))
		     (List.tabulate(lev + 1, fn x => x));


(* ================================== 1 pass ================================ *)
fun pass () = (back(); allweights(); allbias(); forward(); output());

forward();
