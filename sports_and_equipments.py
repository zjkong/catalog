from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Sports, Base, Equipment, User

engine = create_engine('sqlite:///itemcatalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


User1 = User(name='zhijun kong', email='kxx1309@gmail.com')
session.add(User1)
session.commit()


sports1 = Sports(user_id=1, name='Ping Pong')
session.add(sports1)
session.commit()


equipment1 = Equipment(user_id=1, name='Paddle', description='''Players are equipped with a laminated wooden racket covered with rubber on one or two sides depending on the grip of the player. The ITTF uses the term "racket", though "bat" is common in Britain, and "paddle" in the U.S. The wooden portion of the racket, often referred to as the "blade", commonly features anywhere between one and seven plies of wood, though cork, glass fiber, carbon fiber, aluminum fiber, and Kevlar are sometimes used. According to the ITTF regulations, at least 85% of the blade by thickness shall be of natural wood. Common wood types include balsa, limba, and cypress or "hinoki," which is popular in Japan. The average size of the blade is about 6.5 inches (17 cm) long and 6 inches (15 cm) wide. Although the official restrictions only focus on the flatness and rigidness of the blade itself, these dimensions are optimal for most play styles.\nTable tennis regulations allow different surfaces on each side of the racket. Various types of surfaces provide various levels of spin or speed, and in some cases they nullify spin. For example, a player may have a rubber that provides much spin on one side of his racket, and one that provides no spin on the other. By flipping the racket in play, different types of returns are possible. To help a player distinguish between the rubber used by his opposing player, international rules specify that one side must be red while the other side must be black. The player has the right to inspect his opponent's racket before a match to see the type of rubber used and what colour it is. Despite high speed play and rapid exchanges, a player can see clearly what side of the racket was used to hit the ball. Current rules state that, unless damaged in play, the racket cannot be exchanged for another racket at any time during a match.''', sports=sports1)

session.add(equipment1)
session.commit()

equipment2 = Equipment(user_id=1, name='Ball', description='The international rules specify that the game is played with a sphere having a mass of 2.7 grams (0.095 oz) and a diameter of 40 millimetres (1.57 in).The rules say that the ball shall bounce up 24-26 cm (9.4-10.2 in) when dropped from a height of 30.5 cm (12.0 in) onto a standard steel block thereby having a coefficient of restitution of 0.89 to 0.92. The ball is made of celluloid or similar plastic material, colored white or orange, with a matte finish. The choice of ball color is made according to the table color and its surroundings. For example, a white ball is easier to see on a green or blue table than it is on a grey table. Manufacturers often indicate the quality of the ball with a star rating system, usually from one to three, three being the highest grade. As this system is not standard across manufacturers, the only way a ball may be used in official competition is upon ITTF approval (the ITTF approval can be seen printed on the ball). \nThe 40 mm ball was introduced after the 2000 Summer Olympics. However, this created some controversy at the time as the Chinese National Team argued that this was merely to give non-Chinese players a better chance of winning since the new type of ball has a slower speed (a 40 mm table tennis ball is slower and spins less than the original 38 mm one, and at that time, most Chinese players were playing with fast attack and smashes). China won all four Olympic gold medals and three silvers in 2000, and have continued to dominate.', sports=sports1)

session.add(equipment2)
session.commit()


sports2 = Sports(user_id=1, name='Basketball')
session.add(sports2)
session.commit()

equipment1 = Equipment(user_id=1, name='Ball', description='The size of the basketball is also regulated. For men, the official ball is 29.5 inches (74.93 cm) in circumference (size 7, or a "295 ball") and weighs 22 oz (623.69 grams). If women are playing, the official basketball size is 28.5 inches (72.39 cm) in circumference (size 6, or a "285 ball") with a weight of 20 oz (567 grams). In 3x3, a formalized version of the halfcourt 3-on-3 game, the size 6 ball is used in all competitions, even those for men only.', sports=sports2)
session.add(equipment1)
session.commit()


sports1 = Sports(user_id=1, name='Skiing')
session.add(sports1)
session.commit()

equipment1 = Equipment(user_id=1, name='Ski', description='A ski is a narrow strip of semi-rigid material worn underfoot to glide over snow. Substantially longer than wide and characteristically employed in pairs, skis are attached to ski boots with ski bindings, with either a free, lockable, or partially secured heel. For climbing slopes, ski skins (originally made of seal fur, but now made of synthetic materials) can be attached at the base of the ski. \nOriginally intended as an aid to travel over snow, they are now mainly used recreationally in the sport of skiing.', sports=sports1)
session.add(equipment1)
session.commit()

equipment2 = Equipment(user_id=1, name='Ski Boot', description='Ski boots were leather winter boots, held to the ski with leather straps. As skiing became more specialized, so too did ski boots, leading to the splitting of designs between those for alpine skiing and cross-country skiing. \nModern skiing developed as an all-round sport with uphill, downhill and cross-country portions. The introduction of the cable binding started a parallel evolution of binding and boot. The binding looped a strap around the back of the boot to hold it forward into a metal cup at the toe. Boots with the sole extended rearward to produce a flange for the cable to firmly latch to became common, as did designs with semi-circular indentations on the heel for the same purpose. \nEffective cross-country skiing requires the boot to flex forward to allow a striding action, so the boots were designed around a sole piece that allowed forward flexing while still keeping the foot relatively firm side-to-side. The upper portions, the cuff, was relatively soft, designed primarily for comfort and warmth. Modern cross-country ski boots remain almost unchanged since 1950s, although modern materials have replaced leather and other natural fibres.', sports=sports1)
session.add(equipment2)
session.commit()

equipment3 = Equipment(user_id=1, name='Ski Pole', description='Ski poles are used by skiers for balance and propulsion. Modern cross-country ski poles are made from aluminum, fiberglass-reinforced plastic, or carbon fiber, depending on weight, cost and performance parameters. Poles are generally used in alpine skiing, freestyle skiing and nordic skiing and are not usually used in ski jumping, and snowboarding.', sports=sports1)
session.add(equipment3)
session.commit()


sports2 = Sports(user_id=1, name='Tennis')
session.add(sports2)
session.commit()

equipment1 = Equipment(user_id=1, name='Racquets', description='The components of a tennis racquet include a handle, known as the grip, connected to a neck which joins a roughly elliptical frame that holds a matrix of tightly pulled strings. For the first 100 years of the modern game, racquets were of wood and of standard size, and strings were of animal gut. Laminated wood construction yielded more strength in racquets used through most of the 20th century until first metal and then composites of carbon graphite, ceramics, and lighter metals such as titanium were introduced. These stronger materials enabled the production of over-sized racquets that yielded yet more power. Meanwhile, technology led to the use of synthetic strings that match the feel of gut yet with added durability.', sports=sports2)
session.add(equipment1)


sports1 = Sports(user_id=1, name='Field Hocky')
session.add(sports1)
session.commit()

equipment1 = Equipment(user_id=1, name='Field hockey stick', description='Each player carries a "stick" that normally measures between 80-95 cm (31-38") long; shorter or longer sticks are available. Sticks were traditionally made of wood, but are now often made also with fibreglass, kevlar and/or carbon fibre composites. Metal is forbidden from use in field hockey sticks, due to the risk of injury from sharp edges if the stick were to break. The stick has a rounded handle, has a J-shaped hook at the bottom, and is flattened on the left side (when looking down the handle with the hook facing upwards). All sticks are right handed. Left handed sticks are not permitted.\nThere was traditionally a slight curve (called the bow, or rake) from the top to bottom of the face side of the stick and another on the "heel" edge to the top of the handle (usually made according to the angle at which the handle part was inserted into the splice of the head part of the stick), which assisted in the positioning of the stick head in relation to the ball and made striking the ball easier and more accurate.\nThe hook at the bottom of the stick was only recently the tight curve (Indian style) that we have nowadays. The older "English" sticks had a longer bend, making it very hard to use the stick on the reverse. For this reason players now use the tight curved sticks.\nThe handle makes up the about the top third of the stick. It is wrapped in a grip similar to that used on tennis racket. The grip may be made of a variety of materials, including chamois leather, which many players think improves grip in the wet.\nIt was recently discovered that increasing the depth of the face bow made it easier to get high speeds from the dragflick and made the stroke easier to execute. At first, after this feature was introduced, the Hockey Rules Board placed a limit of 50 mm on the maximum depth of bow over the length of the stick but experience quickly demonstrated this to be excessive. New rules now limit this curve to under 25 mm so as to limit the power with which the ball can be flicked.', sports=sports1)
session.add(equipment1)
session.commit()


sports2 = Sports(user_id=1, name='Surfing')
session.add(sports2)
session.commit()

equipment1 = Equipment(user_id=1, name='Surfboards', description='''A surfboard is an elongated platform used in the sport of surfing. Surfboards are relatively light, but are strong enough to support an individual standing on them while riding a breaking wave. They were invented in ancient Hawaii, where they were known as papa he'e nalu in the Hawaiian language; they were usually made of wood from local trees, such as koa, and were often over 15 feet (5 m) in length and extremely heavy. Major advances over the years include the addition of one or more fins on the bottom rear of the board to improve directional stability, and numerous improvements in materials and shape.\nModern surfboards are made of polyurethane or polystyrene foam covered with layers of fiberglass cloth, and polyester or epoxy resin. The result is a light and strong surfboard that is buoyant and maneuverable. Recent developments in surfboard technology have included the use of carbon fiber. Each year, approximately 400,000 surfboards are manufactured.''', sports=sports2)
session.add(equipment1)


sports1 = Sports(user_id=1, name='Kendo')
session.add(sports1)
session.commit()

equipment1 = Equipment(user_id=1, name='shinai', description='Shinai is a weapon used for practice and competition in kendo representing a Japanese sword. Shinai are also used in other martial arts, but may be styled differently from kendo shinai, and represented with different characters.', sports=sports1)
session.add(equipment1)
session.commit()

equipment2 = Equipment(user_id=1, name='Men', description='''Men is one of the five strikes in kendo (along with tsuki, do, hidari kote and migi kote). It is a long slashing stroke that falls on the centre-line of the head. Men also designates the movement, the target, and the part of the kendo armour that covers the whole head. The kiai for this strike, as for all strikes in kendo, is the name of the target area.\nThe men strike is executed as a vertical slash in numerous ways. The basic technique is to raise the shinai or sword such that it is forty-five degrees from the vertical behind the swordsman's head, with the tip either directly above the tsuba or directly above the right point of the acromion (as viewed from the front), and the left hand exactly one fist from the forehead. From this position, power is given from the left hand to bring the sword down. At the point at which the shinai strikes the opponent, both right and left hands should be squeezed for a second which is called tenouchi, also the right arm must be exactly parallel with the ground and at shoulder height. The shoulders should be relaxed. At the moment of the strike, both hands should flex inwards in a movement called shibori, the Japanese verb for "to wring out (a cloth)". This flexion should only be maintained for an instant. It serves to make the strike clean, fast, and bring the shinai off the target area such that a follow-up strike can be made with great ease.\nSa-yu men strikes - or hidari (left) and migi (right) men, respectively - are variants on the men strike and are made at points either fifteen degrees to the left or right of centreline as drawn from the point between the eyes to the top of the head. This strike is made only with a subtle variation on the basic men technique. The tip is simply directed slightly more left or right as it is cocked back into the ready position.\nMen is the first and most practiced strike in kendo. It is a favourable attack for those with a height advantage.''', sports=sports1)
session.add(equipment2)
session.commit()

equipment3 = Equipment(user_id=1, name='Do', description='Do (breastplate or cuirass) is one of the major components of Japanese armour worn by the samurai class and foot soldiers (ashigaru) of feudal Japan.', sports=sports1)
session.add(equipment3)
session.commit()


sports2 = Sports(user_id=1, name='Weightlifting')
session.add(sports2)
session.commit()

equipment1 = Equipment(user_id=1, name='Barbell', description='''A barbell is a piece of exercise equipment used in weight training, bodybuilding, weightlifting and powerlifting, consisting of a long bar with weights attached at each end.\nBarbells range in length from 4 feet (1.2 m) to above 8 feet (2.4 m), although bars longer than 2.2 metres (7.2 ft) are used primarily by powerlifters and are not commonplace. The central portion of the bar varies in diameter from 25 millimetres (0.98 in) to 2 inches (51 mm) (e.g. Apollon's Axle), and is often engraved with a knurled crosshatch pattern to help lifters maintain a solid grip. Disc weights (plates) are slid onto the outer portions of the bar to increase or decrease the desired total weight. These weights are often secured with collars to prevent them from sliding off during the exercise, which can result in injuries, or flinging the unevenly-loaded barbell through the air.''', sports=sports2)
session.add(equipment1)

equipment2 = Equipment(user_id=1, name='Bumper Plates', description='''Plates used in Olympic lifting, which are often termed "bumper" plates, need to be able to be safely dropped from above head height and as such are coated in solid rubber. General strength/hypertrophy training plates are made from cast iron and are considerably cheaper.''', sports=sports2)
session.add(equipment2)
session.commit()


sports1 = Sports(user_id=1, name='Indoor Climbing')
session.add(sports1)
session.commit()

equipment1 = Equipment(user_id=1, name='Ropes', description='Climbing ropes are typically of kernmantle construction, consisting of a core (kern) of long twisted fibres and an outer sheath (mantle) of woven coloured fibres. The core provides about 80% of the tensile strength, while the sheath is a durable layer that protects the core and gives the rope desirable handling characteristics.\nRopes used for climbing can be divided into two classes: dynamic ropes and low elongation ropes (sometimes called "static" ropes). Dynamic ropes are designed to absorb the energy of a falling climber, and are usually used as Belaying ropes. When a climber falls, the rope stretches, reducing the maximum force experienced by the climber, their belayer, and equipment. Low elongation ropes stretch much less, and are usually used in anchoring systems. They are also used for abseiling (rappelling) and as fixed ropes climbed with ascenders.', sports=sports1)
session.add(equipment1)
session.commit()


sports2 = Sports(user_id=1, name='Angling')
session.add(sports2)
session.commit()

equipment1 = Equipment(user_id=1, name='Rod', description='''A fishing rod is a long, flexible length of glass fibre composite, carbon fibre composite or, classically, bamboo, used to catch fish. In contrast with subsistence and commercial fishing, which usually involve nets, fishing rods are typically used in recreational fishing and competitive casting. At its simplest, a fishing rod is a simple stick or pole with a line ending in a hook (formerly known as an angle, hence the term angling). To entice fish, bait is impaled on the hook or lures with hooks are attached to the line. Line is generally stored on a reel which may assist in landing a fish. There are various types of fishing rods designed for specific types of fishing. Fly rods are used to cast artificial flies, spinning rods and bait casting rods are designed to cast baits or lures. Ice fishing rods are designed to fish through small holes in ice covered lakes. Trolling rods are designed to drag bait or lures behind moving boats. Fishing rods come in a variety of sizes, actions, lengths and configurations depending on whether they are to be used for small, medium or large fish or in different fresh or salt water situations. Contemporary fishing rods are constructed of either graphite or fiberglass materials. Fishing rod length may vary between 2 and 20 feet (0.61 and 6.10 m) depending on application.''', sports=sports2)
session.add(equipment1)

equipment2 = Equipment(user_id=1, name='Baits', description='''Fishing bait is any substance used to attract and catch fish, e.g. on the end of a fishing hook, or inside a fish trap. Traditionally, nightcrawlers, insects, and smaller bait fish have been used for this purpose. Fishermen have also begun using plastic bait and, more recently, electronic lures, to attract fish.\nStudies show that natural baits like croaker and shrimp are more recognized by the fish and are more readily accepted. Which of the various techniques a fisher may choose is dictated mainly by the target species and by its habitat. Bait can be separated into two main categories: artificial baits and natural baits.''', sports=sports2)
session.add(equipment2)
session.commit()

equipment3 = Equipment(user_id=1, name='Hooks', description='''A fish hook or fishhook is a device for catching fish either by impaling them in the mouth or, more rarely, by snagging the body of the fish. Fish hooks have been employed for centuries by fishermen to catch fresh and saltwater fish. In 2005, the fish hook was chosen by Forbes as one of the top twenty tools in the history of man.[1] Fish hooks are normally attached to some form of line or lure device which connects the caught fish to the fisherman. There is an enormous variety of fish hooks in the world of fishing. Sizes, designs, shapes, and materials are all variable depending on the intended purpose of the fish hook. Fish hooks are manufactured for a range of purposes from general fishing to extremely limited and specialized applications. Fish hooks are designed to hold various types of artificial, processed, dead or live baits (bait fishing); to act as the foundation for artificial representations of fish prey (fly fishing); or to be attached to or integrated into other devices that represent fish prey (lure fishing).''', sports=sports2)
session.add(equipment3)
session.commit()


items1 = session.query(Sports).all()
items2 = session.query(Equipment).all()
for i in items1:
    print i.id, i.name

for i in items2:
    print i.sports_id, i.name
